from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class Link(models.Model):
    # DB Fields
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    identifier = models.SlugField(max_length=20, unique=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    active = models.BooleanField(default=True)

