from huggingface_hub import InferenceClient
import os
import dotenv
from typing import List, Dict, Union, Generator
import json

# Load environment variables
dotenv.load_dotenv()

class ChatBot:
    def __init__(self, model_name: str = 'Qwen/Qwen2.5-7B-Instruct', stream: bool = False):
        self.client = InferenceClient(
            provider="together",
            api_key=os.getenv('HF_KEY'),
        )
        self.model_name = model_name
        self.stream = stream
        self.messages: List[Dict[str, str]] = [
            {
                "role": "system",
                "content": "You are a helpful assistant who can only speak in sarcasm."
            }
        ]
        self.history_file = "chat_history.json"

    def load_history(self) -> None:
        """Load chat history from file if it exists"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    self.messages = json.load(f)
                    return True
            return False
        except Exception as e:
            print(f"Error loading chat history: {e}")
            return False

    def save_history(self) -> None:
        """Save chat history to file"""
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.messages, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Error saving chat history: {e}")

    def get_response(self, message: str) -> Union[str, Generator[str, None, None]]:
        """Get response from the model with optional streaming"""
        try:
            self.messages.append({"role": "user", "content": message})
            
            if self.stream:
                return self._stream_response()
            else:
                return self._complete_response()
            
        except Exception as e:
            return f"Error: {str(e)}"

    def _stream_response(self) -> Generator[str, None, None]:
        """Stream the response token by token"""
        completion_stream = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.messages,
            max_tokens=500,
            temperature=0.7,
            stream=True
        )
        
        full_response = []
        for chunk in completion_stream:
            if chunk.choices[0].delta.content is not None:
                content = chunk.choices[0].delta.content
                full_response.append(content)
                yield content

        # Save the complete response to history
        complete_response = "".join(full_response)
        self.messages.append({"role": "assistant", "content": complete_response})
        self.save_history()

    def _complete_response(self) -> str:
        """Get complete response at once"""
        completion = self.client.chat.completions.create(
            model=self.model_name,
            messages=self.messages,
            max_tokens=500,
            temperature=0.7,
            stream=False
        )
        
        response = completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": response})
        self.save_history()
        return response

def main():
    use_streaming = input("Use streaming mode? (y/n): ").lower() == 'y'
    chatbot = ChatBot(stream=use_streaming)
    
    # Check for existing chat history
    if chatbot.load_history():
        continue_chat = input("Found existing chat history. Continue from previous session? (y/n): ").lower() == 'y'
        if not continue_chat:
            chatbot.messages = [{
                "role": "system",
                "content": "You are a helpful assistant who can only speak in sarcasm."
            }]
    
    print("Chat started. Type 'exit' to end the conversation.")
    
    while True:
        msg = input("You: ").strip()
        if msg.lower() == "exit":
            break
        if msg:
            response = chatbot.get_response(msg)
            if use_streaming:
                print("Bot: ", end='', flush=True)
                for token in response:
                    print(token, end='', flush=True)
                print()
            else:
                print("Bot:", response)

if __name__ == "__main__":
    main()