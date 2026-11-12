from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
import uuid


from .manager import UserManager



class User(AbstractBaseUser, PermissionsMixin):



    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    phone_number = models.CharField(max_length=11, unique=True, 
    validators=[
        RegexValidator(
        regex=r'^09\d{9}$',
        message='Phone number must be in this format: 09xxxxxxxxx'
            )
        ]
    )
    is_phone_verified = models.BooleanField(default=False)

    email = models.EmailField(max_length=225, unique=True)
    is_email_verified = models.BooleanField(default=False)

    first_name = models.CharField(max_length=125, blank=False)
    last_name = models.CharField(max_length=125, blank=False)
    

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    terms_accepted = models.BooleanField(default=False)
    terms_accepted_at = models.DateTimeField(null=True, blank=True)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']


    objects = UserManager()

    class Meta:

        ordering = ['-created_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

        indexes = [
            models.Index(fields=['created_at'], name='created_at_idx'),
        ]



    @property
    def is_fully_verified(self):
        return self.is_phone_verified and self.is_email_verified


    def __str__(self):
        return f"{self.phone_number}-{self.get_full_name()}"

    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


    def deactivate(self):
        if self.is_active:
            self.is_active = False
            self.save(update_fields=['is_active', 'updated_at'])

        return None

    def activate(self):
        if not self.is_active:
            self.is_active = True
            self.save(update_fields=['is_active', 'updated_at'])

        return None
