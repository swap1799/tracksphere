from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "core_organization"


class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('MANAGER', 'Manager'),
        ('DEVELOPER', 'Developer'),
        ('VIEWER', 'Viewer'),
    )

    email = models.EmailField()
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,null=True,blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='VIEWER')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    class Meta:
        unique_together = ('email', 'organization')
        db_table = "core_user"
        