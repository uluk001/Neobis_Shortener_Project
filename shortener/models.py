from django.db import models

# Create your models here.
from django.db import models

class URL(models.Model):
    original_url = models.URLField()
    shortened_url = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
