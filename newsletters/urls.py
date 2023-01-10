from .views import newsletter_signup, newsletter_unsuscribe
from django.urls import path

app_name = 'newsletters'

urlpatterns = [
    path('optin/', newsletter_signup, name='optin'),
    path('unsuscribe/', newsletter_unsuscribe, name='unsuscribe'),
]