from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields  import GenericForeignKey
# Create your models here.



class Tag(models.Model):
    label = models.CharField(max_length = 255)

class TaggedItems(models.Model):
    tag = models.ForeignKey(Tag , delete_on = models.CASCADE)


    content_type = models.ForeignKey(Tag , delete_on = models.CASCADE)
    content_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()






