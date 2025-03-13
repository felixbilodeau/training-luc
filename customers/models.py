from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    address = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
