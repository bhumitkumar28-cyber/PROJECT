document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');
  if (!form) return;

  form.addEventListener('submit', () => {
    const btn = form.querySelector('button[type="submit"]');
    if (btn) {
      btn.dataset.originalText = btn.textContent;
      btn.textContent = 'Logging in...';
      btn.disabled = true;
    }
  });
});