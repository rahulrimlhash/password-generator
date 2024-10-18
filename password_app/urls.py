from django.urls import path
from .views import home, password_generate


urlpatterns = [
    path('', home, name='home'),
     path('password/', password_generate, name='password_generate'),
]
