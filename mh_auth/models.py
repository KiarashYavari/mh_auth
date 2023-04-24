from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.apps import apps
from django.contrib.auth.hashers import make_password

# Create your models here.

# custom User Model Manager

class AccountUserManager(BaseUserManager):
    def _create_user(self, password, first_name, last_name, **extra_fields):
               
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        # username = GlobalUserModel.normalize_username(username)
        user = self.model(first_name=first_name, last_name=last_name, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_user(self, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(first_name, last_name, password, **extra_fields)
    
        
    def create_superuser(self, password, first_name, last_name, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(password, first_name, last_name, **extra_fields)


# custom User Model 

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    
    # email field is used as a username for user
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = AccountUserManager()    
    
        
    def __str__(self):
        return f'{self.email}'
