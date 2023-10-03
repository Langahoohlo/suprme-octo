# # tasks.py (inside one of your Django apps)
# from celery import shared_task
# from datetime import timedelta
# from django.utils import timezone
# from .models import Item  # Replace with your actual model

# @shared_task
# def set_is_verified_to_false():
#     # Calculate the date 3 days ago
#     one_minute_ago = timezone.now() - timedelta(minutes=1)
    
#     # Update the is_verified field to False for instances older than 3 days
#     Item.objects.filter(is_verified=True, created_at__lt=one_minute_ago).update(is_verified=False)
