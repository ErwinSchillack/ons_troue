var slideIndex = 1;
showSlides(slideIndex);

function moveSlide(n) {
  showSlides(slideIndex += n);
}

document.addEventListener('DOMContentLoaded', function() {
  showSlides(slideIndex); // Ensure the first slide is shown when the document is ready
});

var slideIndex = 1;
function moveSlide(n) {
  showSlides(slideIndex += n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("slide");
  if (n > slides.length) {slideIndex = 1;}
  if (n < 1) {slideIndex = slides.length;}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slides[slideIndex-1].style.display = "block"; // Ensure it's 'block', not 'flex'
}

// document.addEventListener('DOMContentLoaded', function() {
//   showSlides(slideIndex);
// });

setInterval(function() { moveSlide(1); }, 5000); // Adjust time as necessary
