from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
class Details(models.Model):
    id = models.UUIDField(unique=True,default=uuid.uuid4,primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100,default='')
    regis = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    block = models.CharField(max_length=50)
    agreement = models.BooleanField(default=False,help_text="You need to agree to get OD")

    def __str__(self):
        return self.user.username
    