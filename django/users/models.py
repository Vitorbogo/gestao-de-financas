from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

from uuid import uuid4


class UserProfileManager(BaseUserManager):
    """Database model for user managers in the system"""

    def create_user(self, email:str, first_name:str, last_name:str, password:str=None):
        """Create a new user in the database"""
        if not email:
            raise ValueError("User must have a email")
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email:str, first_name:str, last_name:str, password:str):
        """Create and save a new super user"""
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self) -> str:
        return self.first_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
