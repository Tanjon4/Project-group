from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    SEX_TYPES = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    sex = models.CharField(max_length=1, choices=SEX_TYPES)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
