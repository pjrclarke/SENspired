document.addEventListener('DOMContentLoaded', function() {
    // Get the current page URL
    var currentPage = window.location.pathname;

    // Check if the current page is index.html
    if (currentPage === 'event/index.html') {
        // Add a specific class to the body element
        document.body.classList.add('index-page');
    } else {
        // Remove the class if not on index.html
        document.body.classList.remove('index-page');
    }
});