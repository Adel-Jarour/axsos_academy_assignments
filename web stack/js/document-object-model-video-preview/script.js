const previewVideo = document.querySelector("#previewVideo");
const videoFrame = document.querySelector(".video-frame");

const playPreview = async () => {
    if (!previewVideo) return;
    previewVideo.muted = true;
    previewVideo.currentTime = 0;
    try {
        await previewVideo.play();
        videoFrame?.classList.add("is-hovered");
    } catch (err) {
        // Autoplay may be blocked; keep muted and wait for user interaction.
        console.warn("Preview play blocked:", err);
    }
};

const pausePreview = () => {
    if (!previewVideo) return;
    previewVideo.pause();
    previewVideo.currentTime = 0;
    videoFrame?.classList.remove("is-hovered");
};

if (previewVideo) {
    previewVideo.addEventListener("mouseenter", playPreview);
    previewVideo.addEventListener("mouseleave", pausePreview);
    previewVideo.addEventListener("focus", playPreview);
    previewVideo.addEventListener("blur", pausePreview);

    // For touch devices: tap to toggle preview.
    previewVideo.addEventListener("click", () => {
        if (previewVideo.paused) {
            playPreview();
        } else {
            pausePreview();
        }
    });
}
