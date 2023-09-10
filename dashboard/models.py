from django.db import models
from django.contrib.auth.models import User
from item.models import Item

class MyMedia(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)  # Allow NULL for item
    image = models.ImageField(upload_to='my_model_images/', null=True, blank=True)  # For images
    video = models.FileField(upload_to='my_model_videos/', null=True, blank=True)  # For videos
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Allow NULL for created_by
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

