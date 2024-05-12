from django.shortcuts import render,redirect
from django.contrib.auth import logout, login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserProfileForm
from .models import Profile_image
import requests
from django.contrib.auth.decorators import login_required 

# Create your views here.
def index(request):
    return render(request, 'index.html')
def profile(request):
    return render(request, 'profile.html')
def details(request):
    return render(request, 'photo-details.html')
def profile_details(request):
    return render(request, 'profile-details.html')
def edit_profile(request):
    return render(request, 'edit-profile.html')
def donate(request):
    return render(request, 'donate.html')
def donate_faq(request):
    return render(request, 'donate-faq.html')
def classroom(request):
    return render(request, 'classroom.html')
def jobs(request):
    return render(request, 'jobs.html')
def faqs(request):
    return render(request, 'faqs.html')
def customer_support(request):
    return render(request, 'customer_support.html')
def terms(request):
    return render(request, 'terms-of-service.html')
def ways_to_give(request):
    return render(request, 'ways-to-give.html')


def profile_image(request):
    profile_image = Profile_image.objects.filter(user=request.user)
    return render(request, 'profile.html', {'profile_image': profile_image})

@login_required
def update_profile(request):
    user_profile = request.user
    if requests:
        form = UserProfileForm(request.POST, instance=user_profile)
        form.save() 
        return redirect('update_profile')
    else:
       form = UserProfileForm(instance=user_profile)
       return(request, 'profile', {'form':form})

def logout_view(request):
    # Clear any user-specific data from the session
    request.session.pop('cart', None)  # Assuming 'cart' is the key storing cart items

    # Perform logout
    logout(request)

    # Redirect to the index page
    return redirect('/')

def login_view(request):
    if request.method == 'POST':
        # Your existing login form handling

        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Check if the user is authenticated
            if user.is_authenticated:
                # Transfer cart data from session to user's account
                if 'cart' in request.session:
                    # Assuming 'cart' is the key storing cart items
                    user.profile.cart = request.session['cart']
                    user.profile.save()

                # Perform login
                login(request, user)
                return redirect('index')

    # Handle unsuccessful login here
    return render(request, 'login.html', {'error': 'Invalid login credentials'})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after registration
            return redirect('index')  # Redirect to the index page after successful registration
        else:
            print(form.errors)
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

# from django.shortcuts import render, redirect
# from .forms import ProfilePictureForm

# def update_profile_picture(request):
#     if request.method == 'POST':
#         form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = ProfilePictureForm(instance=request.user)
#     return render(request, 'update_profile_picture.html', {'form': form})
