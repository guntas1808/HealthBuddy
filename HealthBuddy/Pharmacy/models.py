from django.db import models
from django.contrib.auth.models import Permission, User

# Create your models here.
class Medicine(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=500)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name