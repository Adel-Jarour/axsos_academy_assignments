function removeBlanks(str) {
  let result = "";
  for (let char of str) {
    if (char !== " ") {
      result += char;
    }
  }
  return result;
}

// console.log(removeBlanks("Adel Ghassan Adel Jarour, Flutter Developer ."));

function getDigit(str) {
  let result = "";
  for (let char of str) {
    if (char == Number(char) && char !== " ") {
      result += char;
    }
  }
  return result;
}

// console.log(getDigit("Adel Jarour, I am 25 years old, I speak 2 languages."));

function acronym(str = "") {
  let result = "";
  let words = str.split(" ");
  for (let i = 0; i < words.length; i++) {
    result += words[i][0].toUpperCase();
  }
  return result;
}

// console.log(acronym("Adel Jarour - Flutter Developer"));

function countNonSpaces(str) {
  let result = 0;
  let words = str.split(" ");
  for (let i = 0; i < words.length; i++) {
    result += words[i].length;
  }
  return result;
}

// console.log(countNonSpaces("Adel Jarour - Flutter Developer."));

function removeShortStrings(arr, minLength) {
  let result = Array();
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].length >= minLength) {
      result.push(arr[i]);
    }
  }
  return result;
}

console.log(
  removeShortStrings(["Adel", "Good morning", "Flutter", "Hi", "Bootcamp"], 5),
);
