from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    tag = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = models.GenericForeignKey()

