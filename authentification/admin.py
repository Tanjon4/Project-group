from django.contrib import admin
from .models import Customer

# Register your models here.
# Customer admin
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'city', 'sex', 'role', 'created_at')
    search_fields = ('user__username', 'user__email', 'city')
    def email(self, obj):
        return obj.user.email

admin.site.register(Customer, CustomerAdmin)
