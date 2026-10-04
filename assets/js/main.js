// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuIcon = document.querySelector('.mobile-menu-icon');
    const mobileMenu = document.querySelector('.mobile-menu');
    
    if (mobileMenuIcon && mobileMenu) {
        mobileMenuIcon.addEventListener('click', function() {
            mobileMenu.classList.toggle('active');
        });
    }
    
    // Close mobile menu when clicking a link
    const mobileLinks = document.querySelectorAll('.mobile-menu a');
    mobileLinks.forEach(link => {
        link.addEventListener('click', function() {
            mobileMenu.classList.remove('active');
        });
    });
    
    // Add fade-in-up animation to elements on scroll
    const fadeElements = document.querySelectorAll('.fade-in-up');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1
    });
    
    fadeElements.forEach(element => {
        observer.observe(element);
    });
    
    // Initialize animations
    document.documentElement.classList.add('js-ready');
});