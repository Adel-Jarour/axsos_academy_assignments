let likes = 0;

function addLike() {
  likes++;

  const count = document.getElementById("likeCount");
  const wrapper = document.getElementById("likeWrapper");

  count.innerText = likes;

  if (likes > 0) {
    wrapper.style.display = "inline";
  }
}
