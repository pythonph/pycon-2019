from django.db import models

# Create your models here.


class Audit(models.Model):
    created_time = models.DateTimeField(auto_add_now=True)
    modified_time = models.DateTimeField(auto_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
