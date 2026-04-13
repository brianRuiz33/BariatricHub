from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path('about/', views.about, name='about'),
    # Procedures
    path('gastric-sleeve/', views.sleeve, name="gastric_sleeve"),
    path('endoscopic-gastric-sleeve/', views.endoscopic, name="endoscopic"),
    path('gastric-balloon/', views.balloon, name="balloon"),
    path('one-anastomosis-gastric-bypass/', views.one_bypass, name="one"),
    path('roux-en-y-gastric-bypass/', views.roux, name="roux"),
    path('intestinal_bipartition/', views.bipartition, name="bipartition"),


    path('travel/', views.travel, name="travel"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('dashboard/', views.dashboard, name="dashboard"), 
    path('questions/', views.questions, name="questions"), 

    # Forms
    path("contact/submit/", views.contact_submit, name="contact_submit"),
    path("appointment/create/", views.appointment_create, name="appointment_create"),
    path("dashboard/appointment/update/", views.appointment_update, name="appointment_update")
]