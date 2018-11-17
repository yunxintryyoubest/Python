from django.db import models

# Create your models here.


class book1(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    pub_date=models.DateField()