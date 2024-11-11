"""
To create database table definitions for this application based on the provided data model, you'll need to define Django models for each of the tables.

Specify relationships between these tables using foreign keys.
"""


django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    membership = models.CharField(max_length=255)
    date_joined = models.DateTimeField()

class AppUsage(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    usage_type = models.CharField(max_length=255)
    session_start = models.DateTimeField()
    session_end = models.DateTimeField()
    clicks = models.IntegerField()
    pages_visited = models.IntegerField()
    device = models.CharField(max_length=255)

class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField()
    sender_id = models.ForeignKey(User, related_name='sent_transactions', on_delete=models.CASCADE)
    recipient_id = models.ForeignKey(User, related_name='received_transactions', on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=255) 