from django.db import models
from django.utils import timezone

# Create your models here.


class imagenTabla(models.Model):
    name_img = models.CharField(max_length=50, null=False)
    url_img = models.ImageField(upload_to="img", null=True)
    format_img =models.CharField(max_length=50, null=False)
    created = models.DateTimeField(default=timezone.now)
    edited = models.DateTimeField(blank=True, default=None, null=True)
