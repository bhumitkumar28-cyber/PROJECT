// Helpline Rotator (Auto-rotate every 4s)
const helplines = [
  { number: '+91 81267 09463', details: 'Aligarh Central Blood Bank – All Groups' },
  { number: '+91 99999 88888', details: 'Agra District Hospital – O+ Urgent' },
  { number: '+91 77777 66666', details: 'Mathura Blood Center – AB- Rare' },
  { number: '108', details: 'National Emergency – Toll Free' }
];
let currentHelpline = 0;
const rotatorNumber = document.getElementById('helpline-number');
const rotatorDetails = document.getElementById('helpline-details');
const dotsContainer = document.getElementById('rotator-dots');

function initRotator() {
  helplines.forEach((_, i) => {
    const dot = document.createElement('span');
    dot.classList.add('dot');
    dot.onclick = () => goToHelpline(i);
    dotsContainer.appendChild(dot);
  });
  setInterval(rotateHelpline, 4000);
  rotateHelpline(); // Initial
}
function rotateHelpline() {
  const dots = dotsContainer.querySelectorAll('.dot');
  dots.forEach(d => d.classList.remove('active'));
  dots[currentHelpline]?.classList.add('active');
  
  rotatorNumber.style.transition = 'all 0.5s';
  rotatorDetails.style.transition = 'all 0.5s';
  rotatorNumber.textContent = helplines[currentHelpline].number;
  rotatorDetails.textContent = helplines[currentHelpline].details;
  
  currentHelpline = (currentHelpline + 1) % helplines.length;
}
function goToHelpline(index) {
  currentHelpline = index;
  rotateHelpline();
}

// Modal Controls
function openModal(id) {
  document.getElementById(id).style.display = 'block';
  document.body.style.overflow = 'hidden';
}
function closeModal(id) {
  document.getElementById(id).style.display = 'none';
  document.body.style.overflow = 'auto';
}

// Donor Form Submit (Demo - integrate with Django later)
const donorForm = document.querySelector('.donor-form');
if (donorForm) {
  donorForm.addEventListener('submit', (e) => {
    e.preventDefault();
    alert('✅ Thank you! You are registered. We will verify and notify you.');
    closeModal('donor-modal');
    donorForm.reset();
  });
}

// Smooth Scroll for Nav Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', (e) => {
    e.preventDefault();
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Scroll Animations (Intersection Observer)
const observerOptions = { threshold: 0.1, rootMargin: '0px 0px -50px 0px' };
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
});
document.querySelectorAll('.section, .step-card, .blood-card').forEach(el => observer.observe(el));

// Blood Card Tooltips (Hover show compatibility)
document.querySelectorAll('.blood-card').forEach(card => {
  card.addEventListener('click', () => {
    const group = card.dataset.group;
    const compat = getCompatibility(group);
    alert(`Blood Group ${group}\nReceives: ${compat.receives}\nDonates: ${compat.donates}`);
  });
});
function getCompatibility(group) {
  const compat = {
    'A+': { receives: 'A+, A-, O+, O-', donates: 'A+, AB+' },
    'A-': { receives: 'A-, O-', donates: 'A+, A-, AB+, AB-' },
    // Add all groups similarly
    'O-': { receives: 'O-', donates: 'All' }
  };
  return compat[group] || { receives: 'Custom', donates: 'Custom' };
}

// Navbar Scroll Effect
window.addEventListener('scroll', () => {
  const navbar = document.querySelector('.navbar');
  if (window.scrollY > 100) {
    navbar.style.background = 'rgba(255,255,255,0.98)';
    navbar.style.boxShadow = '0 5px 20px rgba(0,0,0,0.1)';
  } else {
    navbar.style.background = 'rgba(255,255,255,0.95)';
    navbar.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
  }
});

// Initialize
document.addEventListener('DOMContentLoaded', () => {
  initRotator();
});