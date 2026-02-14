from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('gastric-sleeve', views.sleeve, name="gastric_sleeve"),
    path('travel', views.travel, name="travel"),
    path('tables-test', views.table_view, name="tables"), 
    # Forms
    path("contact/submit/", views.contact_submit, name="contact_submit"),
    path("appointment/create/", views.appointment_create, name="appointment_create"),
]