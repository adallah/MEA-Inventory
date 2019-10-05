from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class portal(models.Model):
    # user = models.ForeignKey(User, related_name='portal_user', editable=False,  on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    did = models.IntegerField()
    cid = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)