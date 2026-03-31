let currentInput = "";
let operator = "";
let previousValue = "";

const displayDiv = document.querySelector("#display");

// handle number and decimal button presses
function press(num) {
  if (currentInput === "0" && num !== ".") {
    currentInput = num.toString();
  } else {
    currentInput += num;
  }
  updateDisplay(currentInput);
}

// handle operator selection (+, -, *, /)
function setOP(op) {
  operator = op;
  previousValue = currentInput;
  currentInput = "";
}

// clear the calculator
function clr() {
  currentInput = "0";
  operator = "";
  previousValue = "";
  updateDisplay(currentInput);
}

// actual calculation
function calculate() {
  let result = 0;
  const prev = parseFloat(previousValue);
  const current = parseFloat(currentInput);

  if (isNaN(prev) || isNaN(current)) return;

  if (operator === "+") result = prev + current;
  else if (operator === "-") result = prev - current;
  else if (operator === "*") result = prev * current;
  else if (operator === "/") result = prev / current;

  currentInput = result.toString();
  operator = "";
  updateDisplay(currentInput);
}

function updateDisplay(val) {
  displayDiv.textContent = val;
}
