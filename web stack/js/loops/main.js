console.log("numbers from 1 to 10:");
for (var i = 1; i <= 10; i++) {
  console.log(i);
}

console.log("numbers from 10 to 1:");
for (var i = 10; i >= 1; i--) {
  console.log(i);
}

console.log("even numbers from 1 to 20:");
for (var i = 1; i <= 20; i++) {
  if (i % 2 == 0) {
    console.log(i);
  }
}

console.log("odd numbers from 1 to 20:");
for (var i = 1; i <= 20; i++) {
  if (i % 2 != 0) {
    console.log(i);
  }
}

console.log("sum numbers from 1 to 10:");
var sum = 0;
for (var i = 1; i <= 10; i++) {
  sum += i;
}
console.log(sum);

console.log("FizzBuzz numbers from 1 to 30:");

var result = "";
for (var i = 1; i <= 30; i++) {
  result = "";
  if (i % 3 === 0) result += "Fizz";
  if (i % 5 === 0) result += "Buzz";

  console.log(result || i);
}
