// Function to show or hide the scroll-up button based on scroll position
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("scrollBtn").style.display = "block";
    } else {
        document.getElementById("scrollBtn").style.display = "none";
    }
}

// Function to scroll to the top when the button is clicked
function scrollToTop() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
function scrollToNextSection() {
    // Find the next section
    var nextSection = document.querySelector('.nextSection');

    // Scroll to the top of the next section
    nextSection.scrollIntoView({ behavior: 'smooth' });
}

const toggleBtn = document.querySelector('.toggle_btn')
const toggleBtnIcon = document.querySelector('.toggle_btn i')
const dropdownMenu = document.querySelector('.dropdown_menu')

toggleBtn.onclick = function(){
    dropdownMenu.classList.toggle('open')
    const isOpen =dropdownMenu.classList.contains('open')
    toggleBtnIcon.classList= isOpen ? 'fa-solid fa-xmark':'fa-solid fa-bars'
} 