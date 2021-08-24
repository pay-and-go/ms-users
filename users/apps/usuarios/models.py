from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime 
from django.contrib.auth.models import AbstractBaseUser,  BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('tiene que ingresar correo')
        if not username:
            raise ValueError('tiene que ingresar username')

        user = self.model(
            email=self.normalice_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username, password):
        user = self.create_user(
            email=self.normalice_email(email),
            password= password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 20, unique=True)
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    cedula = models.IntegerField(blank=False, null=False, unique=True,  validators=[MinValueValidator(00000000000), MaxValueValidator(99999999999)])
    mail = models.EmailField(max_length = 254, default='DEFAULT VALUE', unique=True)
    #password = models.CharField(blank=False, null=False,max_length = 20)

    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = ['username']

    objects = UsuarioManager()

    def _str_(self):
        return self.mail

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


    
class Log(models.Model):
    id_user = models.IntegerField(blank=False, null=False, unique=True,  validators=[MinValueValidator(00000000000), MaxValueValidator(99999999999)])
    timestamp = models.DateTimeField(default=datetime.now)
    operation = models.CharField(max_length = 20)
    
# Create your models here.
