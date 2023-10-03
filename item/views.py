from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.conf import settings
import os

from django.urls import NoReverseMatch

from .forms import ItemVerificationForm, NewItemForm, EditItemForm
from .models import Category, Item

def verify_item(request, item_id):
    # Retrieve the item you want to verify
    item = get_object_or_404(Item, pk=item_id)

    # Check if the item is not already verified
    if not item.is_verified:
        # Set is_verified to True and update verified_timestamp
        item.is_verified = True
        item.verified_timestamp = timezone.now()
        item.save()
        
        # You can also perform other actions or render a response here
        # For example, redirect to a success page or return a JSON response
        # return render(request, 'success.html', {'item': item})
        return render(request, 'Success', {'item': item})
    else:
        # The item is already verified, you can handle this case as needed
        return render(request, 'already verified', {'item': item})
        # return render(request, 'already_verified.html', {'item': item})

def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    city = request.GET.get('city', '')  # Get the selected city choice
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(area__icontains=query) | Q(city__icontains=query))

    if city:
        items = items.filter(city=city)  # Filter by selected city

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    if request.method == 'POST':
        form = ItemVerificationForm(request.POST)
        if form.is_valid():
            is_verified = form.cleaned_data.get('is_verified')
            item.is_verified = is_verified
            item.save()

        try:
            # Attempt to redirect to the 'item_detail' page, but don't raise an exception
            return redirect('item_detail', pk=pk)
        
        except NoReverseMatch:
            pass  # Suppress the exception if it occurs

    else:
        form = ItemVerificationForm(initial={'is_verified': item.is_verified})

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        'form': form,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        user_items = Item.objects.filter(created_by=request.user)


        if user_items:
            # User already has an item, redirect to some error page or display a message
            return render(request, 'item/error_item_exists.html', {
                'user_item': user_items
            })

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    # Delete associated media file if it exists
    if item.image:
        media_path = os.path.join(settings.MEDIA_ROOT, str(item.image))
        if os.path.exists(media_path):
            os.remove(media_path)

    # Delete the database record
    item.delete()

    return redirect('dashboard:index')