const video = document.getElementById("previewVideo");

if (video) {
  video.addEventListener("mouseover", () => {
    video.play();
  });

  video.addEventListener("mouseout", () => {
    video.pause();
    video.currentTime = 0;
  });
}
