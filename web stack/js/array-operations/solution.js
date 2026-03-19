function accessingElements() {
  let colors = ["red", "blue", "green", "yellow", "purple"];
  console.log("first element: " + colors[0]);
  console.log("second element: " + colors[1]);

  colors[2] = "orange";
  console.log("third element: " + colors[2]);
}

function traversingAnArray() {
  let numbers = [10, 20, 30, 40, 50];

  console.log("normal order:");
  for (var i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
  }

  console.log("reverse order:");
  for (var i = numbers.length - 1; i >= 0; i--) {
    console.log(numbers[i]);
  }
}

function searchingInAnArray(searchNum = 25) {
  let numbers = [5, 10, 15, 20, 25];
  let position = numbers.indexOf(searchNum);
  if (position !== -1) {
    console.log("Found at position: " + position);
    return;
  }
  console.log("Not Found");
}

function sortingAnArray() {
  let scores = [50, 20, 70, 10, 40];
  // console.log("Ascending order: " + scores.sort((a, b) => a - b));
  // console.log("Descending order: " + scores.sort((a, b) => b - a));

  // let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"];
  // console.log("Alphabetical order: " + names.sort());

  for (let i = 0; i < scores.length; i++) {
    for (let j = i + 1; j < scores.length; j++) {
      if (scores[i] < scores[j]) {
        let temp = scores[i];
        scores[i] = scores[j];
        scores[j] = temp;
      }
    }
  }
  console.log(scores);
}

function insertingElements() {
  let animals = ["dog", "cat", "rabbit"];
  animals.push("elephant");
  animals.unshift("lion");
  let catPosition = animals.indexOf("cat");
  animals.splice(catPosition, 0, "tiger");

  console.log(animals);
}

function deletingElements(removeElement = "banana") {
  let fruits = ["apple", "banana", "cherry", "date"];
  fruits.splice(0, 1);
  fruits.splice(fruits.length - 1, 1);
  let removeIndex = fruits.indexOf(removeElement);
  if (removeElement != null) {
    fruits.splice(removeIndex, 1);
  }
  console.log(fruits);
}

function combiningArrays() {
  let arrays1 = [1, 2, 3];
  let arrays2 = [4, 5, 6];
  let arr = arrays1.concat(arrays2);
  console.log(arr);
}

function splittingAnArray() {
  let items = ["a", "b", "c", "d", "e"];
  let arr1 = items.splice(0, 3);
  let arr2 = items;
  console.log("The first array: " + arr1);
  console.log("The secong array: " + arr2);
}

function filteringElements() {
  let numbers = [1, 5, 10, 15, 20, 25, 30];
  let newArr = numbers.filter((value) => value > 15);
  console.log("All numbers greater than 15: " + newArr);
}

function advancedChallengeRemoveDuplicate(
  duplicateArray = [1, 2, 3, 2, 4, 3, 4, 5],
) {
  // first way
  var result = duplicateArray.filter((value, index) => {
    return duplicateArray.indexOf(value) === index;
  });

  // second way
  // var result = [...new Set(duplicateArray)];

  console.log(result);
}

function advancedChallengeRotateArray(rotateArray = [1, 2, 3, 4, 5], n = 2) {
  for (var i = 0; i < n; i++) {
    const last = rotateArray.pop();
    rotateArray.unshift(last);
  }

  console.log(rotateArray);
}

function bonusChallenge() {
  let arr1 = [1, 3, 5];
  let arr2 = [2, 4, 6];
  let mergedArr = [...arr1, ...arr2];

  for (var i = 0; i < mergedArr.length; i++) {
    for (var j = 0; j < mergedArr.length - 1; j++) {
      if (mergedArr[j] > mergedArr[j + 1]) {
        let temp = mergedArr[j];
        mergedArr[j] = mergedArr[j + 1];
        mergedArr[j + 1] = temp;
      }
    }
  }

  console.log(mergedArr);
}

// exectues all code
// accessingElements();
// traversingAnArray();
// searchingInAnArray();
sortingAnArray();
// insertingElements();
// deletingElements();
// combiningArrays();
// splittingAnArray();
// filteringElements();
// advancedChallengeRemoveDuplicate();
// advancedChallengeRotateArray();
// bonusChallenge();
