from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from dashboard.models import MyMedia
from item.models import Item
from .forms import NewMediaForm

from django.conf import settings
import os


@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })

@login_required
def dashboardv2(request):
    if request.method == 'POST':
        form = NewMediaForm(request.POST, request.FILES)

        # Check if the user already has an item
        # user_items = MyMedia.objects.filter(created_by=request.user)

        if form.is_valid():
            MyMedia = form.save(commit=False)
            MyMedia.created_by = request.user
            MyMedia.save()

            return redirect('/')
    else:
        form = NewMediaForm()

    return render(request, 'dashboard/form.html', {
        'form': form,
        'title': 'New MyModel',
    })

def media(request):
    mymedia = MyMedia.objects.all()[:6]

    return render(request, 'dashboard/myprofile.html', {
        'mymedia': mymedia,
    })

def myprofile_view(request,  created_by_id):
    # Filter media items based on the user's ID using the foreign key relationship
    user_media_list = MyMedia.objects.filter(created_by_id=created_by_id)

    # Assuming you want to get the user associated with this media
    user = user_media_list.first().created_by if user_media_list.exists() else None

    return render(request, 'dashboard/myprofile.html', {'user': user, 'user_media': user_media_list,})

def delete_media(request, media_item_id):
    # Get the media item to be deleted, ensure it exists
    media_item = get_object_or_404(MyMedia, pk=media_item_id)

    # Check if the user has permission to delete this media item
    if request.user == media_item.created_by:
        # Delete the media item
        media_item.delete()
    
    # Redirect back to the profile page
    return redirect('dashboard:myprofile', created_by_id=request.user.id)

