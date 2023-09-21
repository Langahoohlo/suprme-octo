from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class City(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class Item(models.Model):
    CITY_CHOICES = (
        ('Maseru', 'Maseru'),
        ('Berea', 'Berea'),
        ('Hlotse', 'Hlotse'),
        ('Mafeteng', 'Mafeteng'),
        ('Mokhotlong', 'Mokhotlong'),
        ('Butha-Bothe', 'Butha-Bothe'),
        # Add more city choices as needed
    )

    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50, choices=CITY_CHOICES)
    is_verified = models.BooleanField(default=True)
    phone = models.IntegerField(null=True)
    

    def __str__(self):
        return self.name




# class Profile(models.Model):
#     category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
#     description = models.TextField(blank=True, null=True)
#     image = models.ImageField(upload_to='item_images', blank=True, null=True)
#     is_sold = models.BooleanField(default=False)
#     created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     area = models.CharField(max_length=50)
#     district = models.CharField(max_length=50)  # New field for District
#     type = models.CharField(max_length=50)      # New field for Type
#     offline_or_available = models.CharField(max_length=50)  # New field for Offline or Available Status
#
#     def __str__(self):
#         return self.name
