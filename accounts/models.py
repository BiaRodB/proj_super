from django.db import models
from django.contrib.auth.models import User
class administrador(models.Model):
    usuario=models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.first_name

