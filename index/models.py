from django.db import models

# Create your models here.
class user_data(models.Model):
    name = models.CharField(max_length=50)
    file_name = models.CharField(max_length=50)
    file_hash = models.CharField(max_length=50)

class user_veri(models.Model):
    name = models.CharField(max_length=50)
    veri_code = models.CharField(max_length=50)