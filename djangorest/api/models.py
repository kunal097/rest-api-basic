from django.db import models


# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20 , null = True)
    address = models.TextField(max_length=50 , null=True)
    gender = models.CharField(max_length=15 , null=True)



    def __str__(self):
        return self.name







