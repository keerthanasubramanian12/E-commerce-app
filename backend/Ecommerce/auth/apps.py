from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = 'auth'
    label = 'auth_app'  # unique label (Django's built-in uses "auth")