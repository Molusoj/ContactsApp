from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='contact-home'),
    path('cover/', views.cover, name='contact-cover'),

]
