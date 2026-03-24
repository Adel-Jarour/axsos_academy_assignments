// Change profile name
function editProfile() {
  const name = document.getElementById("userName");
  name.innerText = "Lama Mohammed";
}

const requestList = document.querySelector(".card-list");

requestList.addEventListener("click", function (e) {
  const acceptBtn = e.target.closest(".accept-btn");
  const rejectBtn = e.target.closest(".reject-btn");

  if (acceptBtn) {
    accept(acceptBtn);
  }

  if (rejectBtn) {
    reject(rejectBtn);
  }
});

// Accept request
function accept(element) {
  removeRequest(element);

  increaseConnections();
}

// Reject Request
function reject(element) {
  removeRequest(element);
}

function removeRequest(element) {
  /*
    This explanation is for Rand.
    we use the closest method instead of querySelector because:
    - I want to remove the li element, not just the buttton(img).
    - closest method starts from the buttton(img), then moves upward, and returns the nearest ancestor that matches .card-list-item.
    - But the querySelector it searches inside the buttton(img) downward, But the img has no children → result: null.  
  */
  const li = element.closest(".card-list-item");
  li.remove();
  decreaseRequests();
}

// Increase connection count
function increaseConnections() {
  const connectionCount = document.getElementById("connectionCount");
  let count = parseInt(connectionCount.innerText);
  connectionCount.innerText = count + 1 + "+";
}

// Decrease request count
function decreaseRequests() {
  const requestCount = document.getElementById("requestCount");
  let count = parseInt(requestCount.innerText);
  requestCount.innerText = count - 1;
}
