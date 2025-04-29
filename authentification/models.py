from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# Create your models here.
class Customer(models.Model):
    SEX_TYPES = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )

    ROLE_TYPES = (
        ('admin', 'Administrateur'),
        ('client', 'Client'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    sex = models.CharField(max_length=1, choices=SEX_TYPES)
    city = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_TYPES, default='client')
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.role == 'admin':
            admin_count = Customer.objects.filter(role='admin')
            if self.pk is None and admin_count.count() >= 10:
                raise ValidationError("Le nombre maximale d'Admin est 10")

    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"

