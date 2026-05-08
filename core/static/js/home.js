// DOM Content Loaded
document.addEventListener('DOMContentLoaded', function() {
    initAll();
});

function initAll() {
    initNavbar();
    initHelplineRotator();
    initBloodGroups();
    initScrollAnimations();
    initCursorFollower();
    initSmoothScroll();
    initWhatsAppLinks();
}

// Navbar Scroll Effect - SIMPLIFIED
function initNavbar() {
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
}

// Helpline Rotator
const helplines = [
    { number: '+91 81267 09463', details: '24/7 Emergency Support - Agra/Mathura', city: 'Agra' },
    { number: '+91 98765 43210', details: 'Primary Blood Bank Line', city: 'Mathura' },
    { number: '+91 87654 32109', details: 'Secondary Support Line', city: 'Firozabad' }
];

function initHelplineRotator() {
    const rotator = document.getElementById('helpline-rotator');
    const numberEl = document.getElementById('helpline-number');
    const detailsEl = document.getElementById('helpline-details');
    const dotsEl = document.getElementById('rotator-dots');
    
    let currentIndex = 0;
    
    // Create dots
    helplines.forEach((_, index) => {
        const dot = document.createElement('div');
        dot.className = 'rotator-dot';
        if (index === 0) dot.classList.add('active');
        dotsEl.appendChild(dot);
    });
    
    const dots = document.querySelectorAll('.rotator-dot');
    
    function rotateHelpline() {
        const helpline = helplines[currentIndex];
        
        numberEl.style.transform = 'scale(0.9)';
        setTimeout(() => {
            numberEl.textContent = helpline.number;
            numberEl.style.transform = 'scale(1)';
        }, 150);
        
        detailsEl.textContent = helpline.details;
        
        // Update dots
        dots.forEach((dot, index) => {
            dot.classList.toggle('active', index === currentIndex);
        });
        
        currentIndex = (currentIndex + 1) % helplines.length;
    }
    
    rotateHelpline();
    setInterval(rotateHelpline, 4000);
    
    dots.forEach((dot, index) => {
        dot.addEventListener('click', () => {
            currentIndex = index;
            rotateHelpline();
        });
    });
}

// Blood Groups Data
const bloodGroupsData = {
    'A+': 127,
    'A-': 23,
    'B+': 189,
    'B-': 34,
    'O+': 256,
    'O-': 45,
    'AB+': 67,
    'AB-': 12
};

function initBloodGroups() {
    const grid = document.getElementById('blood-groups-grid');
    
    Object.entries(bloodGroupsData).forEach(([group, count]) => {
        const card = document.createElement('div');
        card.className = 'blood-group-card card';
        card.innerHTML = `
            <h3>${group}</h3>
            <div class="count">${count}</div>
            <p>Available Donors</p>
            <button class="btn-hero btn-primary" style="margin-top: 1.5rem; font-size: 1rem; padding: 0.8rem 2rem;">
                Find ${group} Donors
            </button>
        `;
        grid.appendChild(card);
    });
}

// Scroll Animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.card, .section, .step-card, .blood-group-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(50px)';
        el.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
        observer.observe(el);
    });
}

// Smooth Scroll
function initSmoothScroll() {
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
}

// WhatsApp Integration
function openWhatsApp() {
    const message = encodeURIComponent("Hi! I need help with blood donation or finding donors. 📍 Location: Agra/Mathura");
    window.open(`https://wa.me/918126709463?text=${message}`, '_blank');
}

function openDonorForm() {
    const message = encodeURIComponent("Hi! I want to register as a blood donor. 💉 Please send me the donor registration form.");
    window.open(`https://wa.me/918126709463?text=${message}`, '_blank');
}

// Cursor Follower
function initCursorFollower() {
    const cursor = document.querySelector('.cursor-follower');
    
    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
    });
    
    document.querySelectorAll('a, button').forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursor.style.transform = 'scale(2)';
            cursor.style.borderWidth = '3px';
        });
        el.addEventListener('mouseleave', () => {
            cursor.style.transform = 'scale(1)';
            cursor.style.borderWidth = '2px';
        });
    });
}

// Export functions
window.scrollToSection = scrollToSection;
window.openWhatsApp = openWhatsApp;
window.openDonorForm = openDonorForm;

function scrollToSection(sectionId) {
    document.getElementById(sectionId).scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
}
const translations = {
    en: {
        "about.hero_title": "About DonationHub",
        "about.hero_desc": "Connecting generous hearts with those in need. Our mission is to create a world where no one goes without help.",
        "about.our_mission": "Our Mission",
        "about.mission1_title": "Empower Giving",
        "about.mission1_desc": "Make donating simple, transparent, and impactful for everyone.",
        "about.mission2_title": "Build Community",
        "about.mission2_desc": "Connect donors and requesters in a trusted, supportive network.",
        "about.mission3_title": "Global Impact",
        "about.mission3_desc": "Support causes worldwide with secure, efficient platform.",
        "about.stats1": "50K+",
        "about.stats1_label": "Donors",
        "about.stats2": "120K+",
        "about.stats2_label": "Requests Fulfilled",
        "about.stats3": "$2.5M+",
        "about.stats3_label": "Raised",
        "about.our_team": "Our Team",
        "about.team1_name": "John Doe",
        "about.team1_role": "Founder & CEO",
        "about.team2_name": "Jane Smith",
        "about.team2_role": "Tech Lead",
        "about.team3_name": "Mike Johnson",
        "about.team3_role": "UX Designer",
        "about.footer": "© 2024 DonationHub. Making a difference, together."
    },
    hi: {
        "about.hero_title": "डोनेशनहब के बारे में",
        "about.hero_desc": "उदार दिलों को जरूरतमंदों से जोड़ना। हमारा मिशन एक ऐसी दुनिया बनाना है जहाँ कोई भी मदद के बिना न रहे।",
        "about.our_mission": "हमारा मिशन",
        "about.mission1_title": "दान को सशक्त बनाना",
        "about.mission1_desc": "सभी के लिए दान करना सरल, पारदर्शी और प्रभावशाली बनाना।",
        "about.mission2_title": "समुदाय बनाना",
        "about.mission2_desc": "दानदाताओं और जरूरतमंदों को विश्वसनीय नेटवर्क में जोड़ना।",
        "about.mission3_title": "वैश्विक प्रभाव",
        "about.mission3_desc": "सुरक्षित, कुशल प्लेटफॉर्म के साथ विश्व भर में सहायता।",
        "about.stats1": "50K+",
        "about.stats1_label": "दानदाता",
        "about.stats2": "120K+",
        "about.stats2_label": "अनुरोध पूरे",
        "about.stats3": "₹20Cr+",
        "about.stats3_label": "संग्रहित",
        "about.our_team": "हमारी टीम",
        "about.team1_name": "जॉन डो",
        "about.team1_role": "संस्थापक और CEO",
        "about.team2_name": "जेन स्मिथ",
        "about.team2_role": "तकनीकी प्रमुख",
        "about.team3_name": "माइक जॉनसन",
        "about.team3_role": "UX डिजाइनर",
        "about.footer": "© 2024 डोनेशनहब। एक साथ बदलाव लाना।"
    },
    es: {
        "about.hero_title": "Acerca de DonationHub",
        "about.hero_desc": "Conectando corazones generosos con quienes lo necesitan. Nuestra misión es crear un mundo donde nadie se quede sin ayuda.",
        "about.our_mission": "Nuestra Misión",
        "about.mission1_title": "Empoderar la Donación",
        "about.mission1_desc": "Hacer que donar sea simple, transparente e impactante para todos.",
        "about.mission2_title": "Construir Comunidad",
        "about.mission2_desc": "Conectar donantes y solicitantes en una red confiable y solidaria.",
        "about.mission3_title": "Impacto Global",
        "about.mission3_desc": "Apoyar causas mundiales con una plataforma segura y eficiente.",
        "about.stats1": "50K+",
        "about.stats1_label": "Donantes",
        "about.stats2": "120K+",
        "about.stats2_label": "Solicitudes Cumplidas",
        "about.stats3": "$2.5M+",
        "about.stats3_label": "Recaudados",
        "about.our_team": "Nuestro Equipo",
        "about.team1_name": "John Doe",
        "about.team1_role": "Fundador y CEO",
        "about.team2_name": "Jane Smith",
        "about.team2_role": "Líder Técnico",
        "about.team3_name": "Mike Johnson",
        "about.team3_role": "Diseñador UX",
        "about.footer": "© 2024 DonationHub. Haciendo la diferencia, juntos."
    }
};
