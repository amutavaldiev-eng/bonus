from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.name


class History(models.Model):
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=20)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title