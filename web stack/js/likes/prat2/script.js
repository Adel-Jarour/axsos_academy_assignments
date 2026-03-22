function addLike(button) {
  const parent = button.parentElement;

  const likeSpan = parent.querySelector(".likeCount");
  const wrapper = parent.querySelector(".likeWrapper");

  let count = parseInt(likeSpan.innerText);

  count++;
  likeSpan.innerText = count;

  if (count > 0) {
    wrapper.style.display = "inline";
  }
}
