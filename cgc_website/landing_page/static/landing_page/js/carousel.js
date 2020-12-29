
function getCurrentSlideNumber(carouselId) {
    let i;
    const carouselRoot = document.getElementById(carouselId)
    const slides = carouselRoot.getElementsByClassName("carousel-item");
    for (i = 0; i < slides.length; i++) {
        if(slides[i].style.display === "block") {
            return i
        }
    }
    return 0
}

function plusSlides(carouselId, n) {
    const nextSlideNumber = getCurrentSlideNumber(carouselId) + n;
    showSlides(carouselId, nextSlideNumber);
}

function showSlides(carouselId, n) {
    let i;
    const carouselRoot = document.getElementById(carouselId)
    const slides = carouselRoot.getElementsByClassName("carousel-item");
    if (n >= slides.length) {
        n = 0
    }
    if (n < 0) {
        n = slides.length - 1
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[n].style.display = "block";

    // Dirty hack for parallax windows to fix their positions
    jQuery(window).trigger('resize').trigger('scroll');
}

function showFirstSlideOnEachCarousel() {
    let i;
    const carousels = document.getElementsByClassName("carousel-root")
    for (i = 0; i < carousels.length; i++) {
        showSlides(carousels[i].id, 0);
    }
}

window.addEventListener("load", showFirstSlideOnEachCarousel);
// showFirstSlideOnEachCarousel()
