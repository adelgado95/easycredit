from django.db import models
from django.conf import settings
from rest_framework.authtoken.models import Token

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nombres')
    last_name = models.CharField(max_length=255, verbose_name='Apellidos')
    identification = models.CharField(max_length=50, verbose_name='Identificación', null=True)
    address = models.TextField(verbose_name='Dirección', null=True)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)