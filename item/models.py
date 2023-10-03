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
    is_verified = models.BooleanField(default=False)
    verified_timestamp = models.DateTimeField(null=True, blank=True)
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

from django.db import models
from django.utils import timezone

class PaywalledContent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_time = models.DateTimeField()  # Set 24 hours from purchase

class UserPurchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.ForeignKey(PaywalledContent, on_delete=models.CASCADE)
    purchase_time = models.DateTimeField(default=timezone.now)
    item_id = models.PositiveIntegerField()  # Reference to the specific item

    def is_valid(self):
        # Check if the purchase is still valid (within 24 hours)
        return self.purchase_time + timezone.timedelta(hours=24) > timezone.now()
