from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('contact-csv/', views.contact_csv_download, name="contact-csv"),
]

