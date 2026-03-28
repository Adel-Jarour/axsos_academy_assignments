function alawaysHungry(arr) {
  let result = [];
  for (let char of arr) {
    if (char === "food" || char === "Food") {
      result.push('"Yummy"');
    }
  }
  if (result.length === 0) {
    console.log("I`am hungry");
  } else {
    console.log(result.join(", "));
  }
}

alawaysHungry(["Adel", 55, -8, "food", "food"]);

function highPass(arr, cutoff) {
  let filteredArr = [];
  for (let num of arr) {
    if (num > cutoff) {
      filteredArr.push(num);
    }
  }
  return filteredArr;
}

var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result);

function betterThanAverage(arr = []) {
  let sum = 0;
  for (let num of arr) {
    sum += num;
  }
  let average = sum / arr.length;
  let count = 0;
  arr.map((num) => {
    if (num > average) {
      count++;
    }
  });
  return count;
}

var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result);

function reverse(arr) {
  let reversedArr = new Array(arr.length).fill(null);
  let lastElementIndex = arr.length - 1;
  arr.forEach((value, index) => {
    reversedArr[lastElementIndex - index] = value;
  });
  return reversedArr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result);

function fibonacciArray(n) {
  var fibArr = [0, 1];

  if (n === 0) return [];
  if (n === 1) return [0];

  for (var i = 2; i < n; i++) {
    var next = fibArr[i - 1] + fibArr[i - 2];
    fibArr.push(next);
  }
  return fibArr;
}

var result = fibonacciArray(10);
console.log(result);
