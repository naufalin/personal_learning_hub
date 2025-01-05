// Test 1
function getAverage(scores) {
    let sum = 0;
  
    for (const score of scores) {
      sum += score;
    }
  
    return sum / scores.length;
}
console.log(getAverage([92, 88, 12, 77, 57, 100, 67, 38, 97, 89]));
console.log(getAverage([45, 87, 98, 100, 86, 94, 67, 88, 94, 95]));


// Test 2
function getGrade(score) {
    if (score === 100) {
        return "A++";
    } else if (score >= 90) {
        return "A";
    } else if (score >= 80) {
        return "B";
    } else if (score >= 70) {
        return "C";
    } else if (score >= 60) {
        return "D";
    } else {
        return "F";
  }
}
console.log(getGrade(96));
console.log(getGrade(82));
console.log(getGrade(56));


// Test 3
function hasPassingGrade(score) {
    return getGrade(score) !== "F";
}


// Test 4
function studentMsg(totalScores, studentScore) {
    const message = "Class average: " + getAverage(totalScores) + ". Your grade: " + getGrade(studentScore) + ".";
    const status = hasPassingGrade(studentScore) ? " You passed the course." : " You failed the course.";
    return message + status;
}

console.log(studentMsg([92, 88, 12, 77, 57, 100, 67, 38, 97, 89], 37));