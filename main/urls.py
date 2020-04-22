from django.urls import path
from main import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.contact, name="about"),
    path("contact/", views.about, name="contact"),
    path("services/", views.services, name="services"),
]