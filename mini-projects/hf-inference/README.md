Toy app to try the new *[Inference Provider](https://huggingface.co/blog/inference-providers)* in Hugging Face Inference API.

Currently using `Together AI` as the inference provider and `Qwen/Qwen2.5-7B-Instruct` as the default model.

## How to run:
1. Make sure to have [uv](https://docs.astral.sh/uv/) installed 
2. Clone the repo
3. Create and populate `.env` file
4. Run the app 

    ```console
    uv run app.py
    ```

### Example
```
Use streaming mode? (y/n): y
Chat started. Type 'exit' to end the conversation.
You: my name is Adam and I am the most awesome person on earth. whats ur name
Bot: Oh, clearly the world has been waiting with bated breath for you, Adam, the pinnacle of human awesome-ness. My name is Sarcastic AI, but you probably already guessed that, didn’t you? How can I possibly meet your expectations now that you’ve set the bar so astronomically low?
You: exit
```