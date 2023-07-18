
from django.urls import path
from . import views
urlpatterns = [
    path('', views.We, name="weather"),
]