from django.db import models

# Create your models here.
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=11, unique=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []