from django.db import models
from django.contrib.auth.models import AbstractUser
from marketplace.models import Productos, ProductoComprado
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class User(AbstractUser):
    stripe_customer_id = models.CharField(max_length=50)

class UserLibrary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="library" )
    productos = models.ManyToManyField(Productos, blank=True)


    def __str__(self):
        return self.user.email


def post_save_user_receiver(sender, instance, created, **kwargs):
    if created:
        library = UserLibrary.objects.create(user=instance)

        producto_comprado = ProductoComprado.objects.filter(email=instance.email)

        for producto_comprado in producto_comprado:
            library.productos.add(producto_comprado.productos)


post_save.connect(post_save_user_receiver, sender=User)


