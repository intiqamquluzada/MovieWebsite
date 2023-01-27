from django.urls import path
from .views import *

app_name = 'movie'
urlpatterns = [
    path("home", home_view, name='home')
]
