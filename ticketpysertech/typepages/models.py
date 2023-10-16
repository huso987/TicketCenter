from django.db import models
from django.contrib.auth.models import User  # Opsiyonel: Kullanıcı kimlik doğrulama için

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    

    def __str__(self):
        return self.name

class SupportTicket(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=20, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Closed', 'Closed')])

    def __str__(self):
        return self.title

class Solution(models.Model):
    ticket = models.ForeignKey(SupportTicket, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solution for Ticket: {self.ticket.title}"
