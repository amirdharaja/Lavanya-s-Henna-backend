from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from enum import Enum

from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, username, password, first_name=None, phone=None, last_name=None):
        if not username:
            raise ValueError('Email required')
        if not password:
            raise ValueError('Password required')

        user_obj = self.model(username = self.normalize_email(username))

        user_obj.set_password(password)
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.phone = phone

        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username, password, first_name=None, phone=None, last_name=None):
        user = self.create_user(
            username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
        )
        return user



class User(AbstractBaseUser):

    username        =    models.CharField(max_length=255, null=False, unique=True)
    password        =    models.CharField(max_length=255, null=False)
    first_name      =    models.CharField(max_length=255, null=True)
    last_name       =    models.CharField(max_length=255, null=True)
    phone       =    models.CharField(max_length=64, null=True)
    is_active          =    models.BooleanField(default=True)
    is_superuser          =    models.BooleanField(default=True)
    is_staff          =    models.BooleanField(default=True)
    last_login      =    models.DateTimeField(null=True)
    created_at      =    models.DateTimeField(auto_now_add=True)
    updated_at      =    models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
    def get_full_name(self):
        return self.first_name + self.last_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def active(self):
        return self.is_active

    class Meta:
        db_table = "users"
