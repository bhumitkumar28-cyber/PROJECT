// static/donor/js/donor.js
document.addEventListener('DOMContentLoaded', function() {
    // Smooth animations for cards
    const cards = document.querySelectorAll('.glass-card, .stat-card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-10px) scale(1.02)';
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Form submission confirmation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!confirm('Confirm action?')) {
                e.preventDefault();
            }
        });
    });

    // Availability toggle animation
    const availToggle = document.getElementById('id_available');
    if (availToggle) {
        availToggle.addEventListener('change', function() {
            this.parentElement.style.transition = 'all 0.3s ease';
            this.checked ? this.parentElement.classList.add('available') : this.parentElement.classList.remove('available');
        });
    }
});
