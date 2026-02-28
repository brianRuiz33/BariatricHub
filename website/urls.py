from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path('about/', views.about, name='about'),
    path('gastric-sleeve/', views.sleeve, name="gastric_sleeve"),
    path('travel/', views.travel, name="travel"),
    path('dashboard/', views.dashboard, name="dashboard"), 
    # Forms
    path("contact/submit/", views.contact_submit, name="contact_submit"),
    path("appointment/create/", views.appointment_create, name="appointment_create"),
]