// How It Works - Interactive Features
document.addEventListener('DOMContentLoaded', function() {
  
  // Language Switcher
  const langBtns = document.querySelectorAll('.lang-btn');
  langBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      // Remove active class from all buttons
      langBtns.forEach(b => b.classList.remove('active'));
      // Add active to clicked button
      this.classList.add('active');
      
      // Change language (Django i18n)
      const lang = this.dataset.lang;
      const urlParams = new URLSearchParams(window.location.search);
      urlParams.set('lang', lang);
      window.location.search = urlParams.toString();
    });
  });
  
  // Tab Functionality
  const tabBtns = document.querySelectorAll('.tab-btn');
  const tabContents = document.querySelectorAll('.tab-content');
  
  tabBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      const targetTab = this.dataset.tab;
      
      // Update active tab button
      tabBtns.forEach(b => b.classList.remove('active'));
      this.classList.add('active');
      
      // Update active tab content
      tabContents.forEach(content => content.classList.remove('active'));
      document.getElementById(targetTab).classList.add('active');
    });
  });
  
  // Smooth Animations on Scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };
  
  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  }, observerOptions);
  
  // Observe all steps and process steps
  document.querySelectorAll('.step, .process-step').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(30px)';
    el.style.transition = 'all 0.6s ease';
    observer.observe(el);
  });
  
  // Hero animations
  setTimeout(() => {
    document.querySelector('.hero h1').style.opacity = '1';
    document.querySelector('.hero h1').style.transform = 'translateY(0)';
  }, 300);
  
  // Mobile menu toggle (if needed)
  const navLinks = document.querySelector('.nav-links');
  if (window.innerWidth <= 768) {
    // Add mobile menu functionality if hamburger needed
  }
});