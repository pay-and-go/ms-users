from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime 
class Usuario(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    cedula = models.IntegerField(blank=False, null=False, unique=True,  validators=[MinValueValidator(00000000000), MaxValueValidator(99999999999)])
    mail = models.EmailField(max_length = 254, default='DEFAULT VALUE')
    password = models.CharField(blank=False, null=False,max_length = 20)
    
    
class Log(models.Model):
    id_user = models.IntegerField(blank=False, null=False, unique=True,  validators=[MinValueValidator(00000000000), MaxValueValidator(99999999999)])
    timestamp = models.DateTimeField(default=datetime.now)
    operation = models.CharField(max_length = 20)
    
# Create your models here.
