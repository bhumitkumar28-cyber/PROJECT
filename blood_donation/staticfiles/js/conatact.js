const translations = {
    en: {
        "contact.hero_title": "Get In Touch",
        "contact.hero_desc": "We're here to help. Contact us anytime!",
        "contact.info_title": "Contact Information",
        "contact.phone_label": "Phone",
        "contact.phone": "+1 (800) 123-4567",
        "contact.email_label": "Email",
        "contact.email": "support@donationhub.com",
        "contact.address_label": "Address",
        "contact.address": "123 Charity Street, Help City, HC 12345",
        "contact.helpline_title": "Emergency Helpline",
        "contact.helpline_number": "24/7: 1-800-HELP-NOW",
        "contact.helpline_desc": "Available for urgent donation requests",
        "contact.form_title": "Send us a Message",
        "contact.form_name": "Your Name",
        "contact.form_email": "Email Address",
        "contact.form_subject": "Subject",
        "contact.form_message": "Message",
        "contact.form_submit": "Send Message"
    },
    hi: {
        "contact.hero_title": "संपर्क करें",
        "contact.hero_desc": "हम आपकी मदद के लिए हैं। कभी भी संपर्क करें!",
        "contact.info_title": "संपर्क जानकारी",
        "contact.phone_label": "फ़ोन",
        "contact.phone": "+91 800 123 4567",
        "contact.email_label": "ईमेल",
        "contact.email": "support@donationhub.com",
        "contact.address_label": "पता",
        "contact.address": "123 चैरिटी स्ट्रीट, हेल्प सिटी, एचसी 12345",
        "contact.helpline_title": "आपातकालीन हेल्पलाइन",
        "contact.helpline_number": "24/7: 1800-HELP-NOW",
        "contact.helpline_desc": "तत्काल दान अनुरोधों के लिए उपलब्ध",
        "contact.form_title": "हमें संदेश भेजें",
        "contact.form_name": "आपका नाम",
        "contact.form_email": "ईमेल पता",
        "contact.form_subject": "विषय",
        "contact.form_message": "संदेश",
        "contact.form_submit": "संदेश भेजें"
    },
    es: {
        "contact.hero_title": "Ponte en Contacto",
        "contact.hero_desc": "Estamos aquí para ayudar. ¡Contáctanos cuando quieras!",
        "contact.info_title": "Información de Contacto",
        "contact.phone_label": "Teléfono",
        "contact.phone": "+1 (800) 123-4567",
        "contact.email_label": "Email",
        "contact.email": "support@donationhub.com",
        "contact.address_label": "Dirección",
        "contact.address": "123 Charity Street, Help City, HC 12345",
        "contact.helpline_title": "Línea de Emergencia",
        "contact.helpline_number": "24/7: 1-800-HELP-NOW",
        "contact.helpline_desc": "Disponible para solicitudes urgentes de donación",
        "contact.form_title": "Envíanos un Mensaje",
        "contact.form_name": "Tu Nombre",
        "contact.form_email": "Dirección de Email",
        "contact.form_subject": "Asunto",
        "contact.form_message": "Mensaje",
        "contact.form_submit": "Enviar Mensaje"
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

document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();
    alert("Thank you for your message! We'll get back to you soon.");
});