function pizzaOven(crust, sauce, cheeses, toppings) {
  return {
    crust: crust,
    sauce: sauce,
    cheeses: cheeses,
    toppings: toppings,
  };
}

var pizza1 = pizzaOven(
  "deep dish",
  "traditional",
  ["mozzarella"],
  ["pepperoni", "sausage"],
);

var pizza2 = pizzaOven(
  "hand tossed",
  "marinara",
  ["mozzarella", "feta"],
  ["mushrooms", "olives", "onions"],
);

var pizza3 = pizzaOven(
  "thin crust",
  "alfredo",
  ["parmesan", "mozzarella"],
  ["chicken", "spinach"],
);

var pizza4 = pizzaOven(
  "stuffed crust",
  "bbq",
  ["cheddar"],
  ["beef", "onions", "peppers"],
);

function randomItem(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

function randomPizza() {
  var crusts = ["deep dish", "hand tossed", "thin crust", "stuffed crust"];
  var sauces = ["traditional", "marinara", "alfredo", "bbq"];
  var cheeses = ["mozzarella", "feta", "cheddar", "parmesan"];
  var toppings = [
    "pepperoni",
    "sausage",
    "mushrooms",
    "olives",
    "onions",
    "chicken",
    "beef",
  ];

  var randomCheeses = [randomItem(cheeses)];
  var randomToppings = [randomItem(toppings), randomItem(toppings)];

  return pizzaOven(
    randomItem(crusts),
    randomItem(sauces),
    randomCheeses,
    randomToppings,
  );
}

console.log("Pizza 1: ", pizza1);
console.log("Pizza 2: ", pizza2);
console.log("Pizza 3: ", pizza3);
console.log("Pizza 4: ", pizza4);

var randomPizzaResult = randomPizza();
console.log("Random Pizza: ", randomPizzaResult);
