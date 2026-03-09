from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.
class Account(AbstractUser):
    email = models.EmailField(unique=True)
    
    groups = models.ManyToManyField(
        Group, 
        related_name='users_set', 
        blank=True,
        help_text='Grupos a los que pertenece este usuario.',
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permission',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='user permissions'
    )
    
    
    def __str__(self):
        return self.username
