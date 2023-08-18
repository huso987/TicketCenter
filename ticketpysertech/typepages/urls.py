from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('NewTicket/', views.newticket),
    path('TicketStatus/', views.statusticket),
    path('Login/', views.getlogin),
    path('Register/', views.getregister),
]
