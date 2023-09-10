from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from item.models import Category, Item
from django.contrib.auth import logout
from PIL import Image

from django.contrib.auth.models import User

from .forms import SignupForm

# def index(request):
#     items = Item.objects.filter(is_sold=False)[0:6]
#     categories = Category.objects.all()
#
#     # Resize images for each item
#     for item in items:
#         img = Image.open(item.image.path)
#         max_size = (800, 800)  # Set your desired maximum size
#         img.thumbnail(max_size)
#         img.save(item.image.path)
#
#     return render(request, 'core/index.html', {
#         'categories': categories,
#         'items': items,
#     })


def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)  # Create a user object but don't save it yet
            user.is_verified = False  # Set is_verified to False
            user.save()  # Save the user object with is_verified set to False

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#
#             return redirect('/login/')
#     else:
#         form = SignupForm()
#
#     return render(request, 'core/signup.html', {
#         'form': form
#     })


def logout_view(request):
    logout(request)
    return redirect('/login/')
    # Replace 'home' with the URL name of your desired redirect page after logout


@login_required
def items(request):
    user = request.user
    user_item = Item.objects.filter(user=user, is_sold=False).first()
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    city = request.GET.get('city', '')  # Get the selected city from the URL
    categories = Category.objects.all()
    items = Item.objects.filter(created_by=request.user)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    last_login_timestamps = {}

    for item in items:
        item_creator = item.created_by
        creator = User.objects.get(id=item.created_by_id)
        last_login_timestamps[item.id] = creator.last_login
    
    # Define the number of items to display per page
    items_per_page = 10  # Adjust this number as needed

    # Create a Paginator instance
    paginator = Paginator(items, items_per_page)
    
    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')
    
    try:
        # Get the items for the current page
        items = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        items = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
        items = paginator.page(paginator.num_pages)

    return render(request, 'core/templates/core/base.html', {
        'user_item': user_item,
        'user': user,
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'selected_city': city,
        'last_login_timestamps': last_login_timestamps,
    })





def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # You can customize this email sending logic as needed
        send_mail(
            'Contact Form Submission',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            'settings.EMAIL_HOST_USER',  # Replace with your email
            [email],  # Replace with recipient's email
            fail_silently=False,
        )

        return HttpResponse('Thank you for your message!')

    return render(request, 'core/contact.html')


def about(request):
    return render(request, 'core/about.html')

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')

def terms_of_use(request):
    return render(request, 'core/terms_of_use.html')

