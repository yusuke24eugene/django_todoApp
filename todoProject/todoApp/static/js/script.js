// Ensure navbar is responsive and collapses on mobile
document.addEventListener("DOMContentLoaded", function () {
    // Get the navbar toggler button and navbar collapse element
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarCollapse = document.getElementById("navbarNav");

    // Add a click event listener to toggle the navbar collapse on mobile
    navbarToggler.addEventListener("click", function () {
        navbarCollapse.classList.toggle("show");
    });
});