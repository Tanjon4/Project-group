from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField() 
    images = models.ImageField(upload_to='services/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
