from .base_models import BaseModel
from django.db import models
from django.contrib.auth.models import User


class Project(BaseModel):
    """
    Project model for basic project information
    """
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    project_pi = models.ForeignKey(User, on_delete=models.CASCADE)
    project_members = models.ManyToManyField(User, blank=True,
                                             related_name="project_members")

    def __str__(self):
        return self.name


class Variable(BaseModel):
    """
    Variables information, every variable should belong to a project
    """
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField()
    collected_datetime = models.DateTimeField(blank=False)
    availability = models.BooleanField(blank=False)
    expiration_date = models.DateField()

    def __str__(self):
        return self.name

