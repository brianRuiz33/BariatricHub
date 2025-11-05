from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('gastric-sleeve', views.sleeve, name="gastric_sleeve"),
    path('travel', views.travel, name="travel")

]