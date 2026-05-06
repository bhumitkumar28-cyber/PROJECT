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

let currentLang = 'en';
document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        currentLang = btn.dataset.lang;
        document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        updateLanguage();
    });
});

function updateLanguage() {
    document.querySelectorAll('[data-translate]').forEach(el => {
        const key = el.dataset.translate;
        el.textContent = translations[currentLang][key] || el.textContent;
    });
    document.documentElement.lang = currentLang;
}