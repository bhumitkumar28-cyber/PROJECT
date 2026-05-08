// Simple language switcher (English ↔ हिंदी)
function setLanguage(lang) {
    // Save to localStorage (or implement server‑side i18n later)
    localStorage.setItem('preferred_lang', lang);

    // Update body class
    document.body.classList.remove('lang-en', 'lang-hi');
    document.body.classList.add('lang-' + lang);

    // Optional: refresh or update text with JS (we keep Django template text for now)
}

// Set default language from localStorage
document.addEventListener('DOMContentLoaded', () => {
    const saved = localStorage.getItem('preferred_lang') || 'en';
    setLanguage(saved);
});