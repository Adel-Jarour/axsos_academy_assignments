function reverseString(str = "hello") {
  let reversed = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }
  return reversed;
}

console.log(reverseString("ADEL"));

function isPalindrome(str) {
  let reversedStr = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversedStr += str[i];
  }
  if (str === reversedStr) {
    return true;
  } else {
    return false;
  }
}
console.log(isPalindrome("dad"));

var vowels = ["a", "e", "i", "u", "o", "A", "I", "O", "E", "U"];

function countVowels(str) {
  var count = 0;
  for (var i = 0; i <= str.length; i++) {
    if (vowels.includes(str[i])) count++;
  }
  return count;
}

console.log(countVowels("adel"));

function findLongestWord(statement = "I am a Barcelona fan") {
  let words = statement.split(" ");
  let longest = words[0];
  for (let i = 1; i < words.length; i++) {
    if (words[i].length > longest.length) {
      longest = words[i];
    }
  }
  console.log("The longest word is: " + longest);
}

findLongestWord();

function feedback(str) {
  let msg = "";
  switch (str) {
    case ("A", "a"):
      msg = "Excellent";
      break;
    case ("B", "b"):
      msg = "Good";
      break;
    case ("C", "c"):
      msg = "You passed";
      break;
    case ("D", "d"):
      msg = "Need improvement";
      break;
    case ("F", "f"):
      msg = "Failed";
      break;
    default:
      msg = "Invalid grade";
  }
  console.log(msg);
}

feedback("d");

function count(str = "Adel 223# ") {
  let countVowels = 0;
  let countDigits = 0;
  let countSpaces = 0;
  let countOthers = 0;
  let vowels = "aoieuAOIEU";
  let nums = "0123456789";
  for (let char of str) {
    if (vowels.includes(char)) {
      countVowels++;
    } else if (nums.includes(char)) {
      countDigits++;
    } else if (char === " ") {
      countSpaces++;
    } else {
      countOthers++;
    }
  }
  return {
    vowels: countVowels,
    digits: countDigits,
    spaces: countSpaces,
    others: countOthers,
  };
}

console.log(count());
