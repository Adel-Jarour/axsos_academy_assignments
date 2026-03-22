// Change profile name
function editProfile() {
  const name = document.getElementById("userName");
  name.innerText = "Lama Mohammed";
}

// Accept request
function accept(element) {
  removeRequest(element);

  const connectionCount = document.getElementById("connectionCount");
  let count = parseInt(connectionCount.innerText);
  connectionCount.innerText = count + 1;
}

// Reject Request
function reject(element) {
  removeRequest(element);
}

function removeRequest(element) {
  const li = element.closest(".card-list-item");
  li.remove();

  const requestCount = document.getElementById("requestCount");
  let count = parseInt(requestCount.innerText);
  requestCount.innerText = count - 1;
}
