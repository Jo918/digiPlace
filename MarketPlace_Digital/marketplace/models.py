from django.db import models
import os
from django.conf import settings

User = settings.AUTH_USER_MODEL

def marketplace_directory_path(instance, filename):
    banner_pic_name='marketplace/productos/{0}/{1}'.format(instance.nombre, filename)
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)
    return banner_pic_name

# Create your models here.

class Productos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="productos")
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(blank=True, null=True, upload_to=marketplace_directory_path)
    slug = models.SlugField(unique=True)

    content_url = models.URLField(blank=True, null=True)
    content_file = models.FileField(blank=True, null=True)

    activo = models.BooleanField(default=True)

    precio = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre


class ProductoComprado(models.Model):
    email = models.EmailField()
    productos = models.ForeignKey(Productos, on_delete=models.CASCADE)
    fecha_compra= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


