# myapp/management/commands/set_is_verified.py

from datetime import timezone
from django.core.management.base import BaseCommand
from .models import Item

class Command(BaseCommand):
    help = 'Set is_verified to False for records 1 minute after being verified'

    def handle(self, *args, **options):
        # Calculate the threshold timestamp (1 minute ago from now)
        threshold_timestamp = timezone.now() - timezone.timedelta(minutes=1)

        # Update records where is_verified is True and verified_timestamp is older than the threshold
        Item.objects.filter(is_verified=True, verified_timestamp__lt=threshold_timestamp).update(is_verified=False)

        self.stdout.write(self.style.SUCCESS('Successfully updated is_verified'))