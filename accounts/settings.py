# Add to settings.py
LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'core:dashboard'
LOGOUT_REDIRECT_URL = 'accounts:user_type_selection'

# Messages settings
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'