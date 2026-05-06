// Blood Requests App JavaScript
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize Bootstrap tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Form validation and submission
    const forms = document.querySelectorAll('.needs-validation');
    Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Real-time countdown timer for deadlines
    initCountdownTimers();

    // Confirm status updates
    document.querySelectorAll('.confirm-status').forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const status = this.dataset.status;
            const messages = {
                'fulfilled': 'Mark this request as fulfilled?',
                'cancelled': 'Cancel this request?'
            };
            if (confirm(messages[status])) {
                this.closest('form').submit();
            }
        });
    });

    // Phone number formatting
    formatPhoneNumbers();

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});

function initCountdownTimers() {
    const deadlineElements = document.querySelectorAll('.deadline-timer');
    deadlineElements.forEach(function(element) {
        const deadlineTime = new Date(element.dataset.deadline).getTime();
        updateCountdown(element, deadlineTime);
        setInterval(() => updateCountdown(element, deadlineTime), 1000);
    });
}

function updateCountdown(element, deadlineTime) {
    const now = new Date().getTime();
    const distance = deadlineTime - now;

    if (distance < 0) {
        element.innerHTML = '<span class="badge bg-danger">OVERDUE!</span>';
        element.className = 'deadline-timer time-danger';
        return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    let timeString = '';
    if (days > 0) timeString += days + 'd ';
    if (hours > 0 || days > 0) timeString += hours + 'h ';
    timeString += minutes + 'm ' + seconds + 's';

    // Color coding
    let className = 'time-left';
    if (distance < 24 * 60 * 60 * 1000) className = 'time-warning'; // Less than 24h
    if (distance < 2 * 60 * 60 * 1000) className = 'time-danger';   // Less than 2h

    element.innerHTML = `<span class="${className}">${timeString}</span>`;
    element.className = `deadline-timer ${className}`;
}

function formatPhoneNumbers() {
    const phoneInputs = document.querySelectorAll('input[type="tel"]');
    phoneInputs.forEach(function(input) {
        input.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length >= 10) {
                value = value.replace(/(\d{3})(\d{3})(\d{4})/, '($1) $2-$3');
            }
            e.target.value = value;
        });
    });
}

// Copy contact number to clipboard
function copyToClipboard(text, button) {
    navigator.clipboard.writeText(text).then(function() {
        const originalText = button.innerHTML;
        button.innerHTML = '<i class="bi bi-check-circle-fill text-success"></i> Copied!';
        button.classList.add('btn-success');
        setTimeout(() => {
            button.innerHTML = originalText;
            button.classList.remove('btn-success');
        }, 2000);
    });
}