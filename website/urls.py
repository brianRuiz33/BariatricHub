from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path('about/', views.about, name='about'),
    path('gastric-sleeve/', views.sleeve, name="gastric_sleeve"),
    path('endoscopic-gastric-sleeve', views.endoscopic, name="endoscopic"),
    path('gastric-balloon', views.balloon, name="balloon"),

    path('travel/', views.travel, name="travel"),
    path('dashboard/', views.dashboard, name="dashboard"), 
    path('questions/', views.questions, name="questions"), 

    # Forms
    path("contact/submit/", views.contact_submit, name="contact_submit"),
    path("appointment/create/", views.appointment_create, name="appointment_create"),
    path("dashboard/appointment/update/", views.appointment_update, name="appointment_update")
]