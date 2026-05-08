# Email (for production)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'

# Twilio SMS (optional)
TWILIO_ACCOUNT_SID = 'your-sid'
TWILIO_AUTH_TOKEN = 'your-token'
TWILIO_PHONE_NUMBER = '+1234567890'