from django.db import models
from django.utils import timezone

from ..cargo.models import Cargo


class Socio(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=15, unique=True)
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_nacimiento = models.DateField()
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
