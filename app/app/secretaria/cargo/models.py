from django.db import models
from django.utils import timezone


class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    cargo = models.TextField(max_length=255, unique=True)
    descripcion = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.cargo
