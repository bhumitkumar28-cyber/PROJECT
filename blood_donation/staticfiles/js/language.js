const translations = {
  en: {
    brand: "BloodCare",
    profile: "Profile",
    password: "Password",
    logout: "Logout",
    login: "Login",
    signup_title: "Create Your Account",
    signup_subtitle: "Choose the type of account you want to create for blood donation services.",
    donor_title: "Donor",
    donor_desc: "Register as a donor to donate blood and help patients in emergency.",
    requester_title: "Requester",
    requester_desc: "Register as a requester to request blood for patients and hospital needs.",
    donor_signup_btn: "Donor Signup",
    requester_signup_btn: "Requester Signup",
    donor_signup_title: "Donor Signup",
    requester_signup_title: "Requester Signup",
    login_title: "Login"
  },
  hi: {
    brand: "ब्लडकेयर",
    profile: "प्रोफाइल",
    password: "पासवर्ड",
    logout: "लॉगआउट",
    login: "लॉगिन",
    signup_title: "अपना खाता बनाएं",
    signup_subtitle: "ब्लड डोनेशन सेवाओं के लिए अपना खाता प्रकार चुनें।",
    donor_title: "दाता",
    donor_desc: "रक्त दान करने और ज़रूरतमंद मरीजों की मदद करने के लिए रजिस्टर करें।",
    requester_title: "अनुरोधकर्ता",
    requester_desc: "मरीजों और अस्पताल की ज़रूरतों के लिए रक्त अनुरोध करने हेतु रजिस्टर करें।",
    donor_signup_btn: "दाता पंजीकरण",
    requester_signup_btn: "अनुरोधकर्ता पंजीकरण",
    donor_signup_title: "दाता पंजीकरण",
    requester_signup_title: "अनुरोधकर्ता पंजीकरण",
    login_title: "लॉगिन"
  }
};

function setLanguage(lang) {
  localStorage.setItem("siteLang", lang);
  document.documentElement.lang = lang;
  document.querySelectorAll("[data-i18n]").forEach(el => {
    const key = el.getAttribute("data-i18n");
    if (translations[lang] && translations[lang][key]) {
      el.innerText = translations[lang][key];
    }
  });
}

document.addEventListener("DOMContentLoaded", () => {
  setLanguage(localStorage.getItem("siteLang") || "en");
});