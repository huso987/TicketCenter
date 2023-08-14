from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('NewTicket/', views.newticket),
    path('TicketStatus/', views.statusticket),
]
