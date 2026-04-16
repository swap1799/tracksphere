from django.db import models
from django.conf import settings
from accounts.models import Organization

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,related_name="projects")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "core_project"