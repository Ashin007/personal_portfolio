from django.db import models

from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)

@receiver(pre_delete, sender=Projects)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
        instance.image.delete(False)