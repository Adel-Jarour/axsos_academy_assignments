// Login / Logout toggle
const loginBtn = document.getElementById("loginBtn");

loginBtn.addEventListener("click", function () {
  if (loginBtn.innerText === "Login") {
    loginBtn.innerText = "Logout";
  } else {
    loginBtn.innerText = "Login";
  }
});

// Like buttons alert
const likeButtons = document.querySelectorAll(".likeBtn");

likeButtons.forEach(function (btn) {
  btn.addEventListener("click", function () {
    alert("Ninja was liked");
  });
});

// Remove Add Definition button
const addDefBtn = document.getElementById("addDefBtn");

addDefBtn.addEventListener("click", function () {
  addDefBtn.remove();
});
