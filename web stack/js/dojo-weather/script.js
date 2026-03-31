const items = document.querySelectorAll(".nav-links a");

items.forEach((item) => {
  item.addEventListener("click", function (event) {
    event.preventDefault(); // prevent page reload
    alert("You clicked on " + this.textContent);
  });
});

const tempSelected = document.getElementById("temperature");
const temps = document.querySelectorAll(".temperature span");

temps.forEach((span) => {
  const value = parseInt(span.textContent);
  span.dataset.celsius = value;
});

tempSelected.addEventListener("change", function () {
  const selectedTempValue = this.value;

  temps.forEach((span) => {
    const celsius = parseInt(span.dataset.celsius);
    let newTemp;

    console.log(selectedTempValue === "fahrenheit");
    if (selectedTempValue === "fahrenheit") {
      newTemp = cToF(celsius);
    } else {
      newTemp = celsius;
    }
    span.textContent = newTemp + "°";
  });
});

function cToF(celsius) {
  return (celsius * 9) / 5 + 32;
}

function fToC(fahrenheit) {
  return ((fahrenheit - 32) * 5) / 9;
}

const banner = document.getElementById("cookieBanner");
const btn = document.getElementById("acceptBtn");

btn.addEventListener("click", function () {
  banner.style.display = "none";
});
