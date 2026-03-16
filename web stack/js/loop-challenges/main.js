function displayOddNumbers() {
  console.log("The Odd numbers between 1 to 20: ");
  for (let i = 1; i <= 20; i++) {
    if (i % 2 != 0) {
      console.log(i);
    }
  }
}

function decreasingMultipleOf(num = 3) {
  console.log("All Number between 0 - 100 that are divisible by " + num + ":");
  for (let i = 100; i >= 0; i--) {
    if (i % num == 0) {
      console.log(i);
    }
  }
}

function printTheSequence() {
  console.log("Print the sequence:");
  for (let i = 4; i >= -3.5; i -= 1.5) {
    console.log(i);
  }
}

function sigma() {
  let sum = 0;
  for (let i = 1; i <= 100; i++) {
    sum += i;
  }
  console.log("The sum of all numbers between 1-100: " + sum);
}

function factorial() {
  let product = 1;
  for (let i = 1; i <= 12; i++) {
    product *= i;
  }
  console.log("The final result of multiplying: " + product);
}

// execute all code
displayOddNumbers();
decreasingMultipleOf();
printTheSequence();
sigma();
factorial();
