// Initialisation WOW.js
new WOW().init();

// Navbar scroll effect
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});

// Back to top button
const backToTopButton = document.querySelector('.back-to-top');

window.addEventListener('scroll', function() {
    if (window.pageYOffset > 300) {
        backToTopButton.classList.add('active');
        backToTopButton.classList.add('animate__fadeIn');
        backToTopButton.classList.remove('animate__fadeOut');
    } else {
        backToTopButton.classList.remove('active');
        backToTopButton.classList.remove('animate__fadeIn');
        backToTopButton.classList.add('animate__fadeOut');
    }
});

backToTopButton.addEventListener('click', function(e) {
    e.preventDefault();
    window.scrollTo({top: 0, behavior: 'smooth'});
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        
        const targetId = this.getAttribute('href');
        if (targetId === '#') return;
        
        const targetElement = document.querySelector(targetId);
        if (targetElement) {
            const navbarHeight = document.querySelector('.navbar').offsetHeight;
            const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navbarHeight;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
            
            // Fermer le menu mobile après le clic
            const navbarToggler = document.querySelector('.navbar-toggler');
            const navbarCollapse = document.querySelector('.navbar-collapse');
            if (navbarCollapse.classList.contains('show')) {
                navbarToggler.click();
            }
        }
    });
});

// Animation du carousel
const heroCarousel = document.getElementById('heroCarousel');
if (heroCarousel) {
    const carousel = new bootstrap.Carousel(heroCarousel, {
        interval: 5000,
        pause: 'hover',
        wrap: true
    });
}

// Effet de survol pour les cartes de services
const serviceCards = document.querySelectorAll('.service-card');
serviceCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.classList.add('shadow-lg');
        this.style.transform = 'translateY(-10px)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.classList.remove('shadow-lg');
        this.style.transform = '';
    });
});

document.addEventListener("DOMContentLoaded", function() {
    var typingText = document.getElementById("typing-text");
    var text = "Bienvenue chez Salon de Beauté!";
    var i = 0;

    function typeWriter() {
        if (i < text.length) {
            typingText.innerHTML += text.charAt(i);
            i++;
            setTimeout(typeWriter, 150);
        }
    }

    typeWriter();
});
