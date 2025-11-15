from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Trip, TripImage, PasswordResetOTP, TripPost, ChatRoom, ChatMessage, UserProfile
from .forms import TripForm, UserRegisterForm, ForgotPasswordForm, OTPVerifyForm, TripPostForm, UserProfileForm
from django.http import JsonResponse

# ===================================================================
# 🧍 USER AUTHENTICATION
# ===================================================================

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


def login_view(request):
    """Handles user login and redirects to home."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'main/login.html')

    return render(request, 'main/login.html')

def logout_view(request):
    """Logs out the current user and redirects to login page."""
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')



    # GET request (just show login form)
    return render(request, 'main/login.html')


    return render(request, 'main/login.html')



# ===================================================================
# 🏠 HOME PAGE
# ===================================================================

def home(request):
    within_country = Trip.objects.filter(category__iexact="Within Country").order_by('-created_at')
    outside_country = Trip.objects.filter(category__iexact="Outside Country").order_by('-created_at')
    tribe_posts = TripPost.objects.all().order_by('-created_at')[:5]

    return render(request, 'main/home.html', {
        'within_country': within_country,
        'outside_country': outside_country,
        'tribe_posts': tribe_posts,
    })


# ===================================================================
# ✈️ TRIPS MANAGEMENT
# ===================================================================

@login_required
def add_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.created_by = request.user
            trip.save()
            
            # Handle multiple image uploads
            images = request.FILES.getlist('additional_images')
            for image in images:
                TripImage.objects.create(trip=trip, image=image)
            
            messages.success(request, "Trip added successfully!")
            return redirect('home')
    else:
        form = TripForm()
    return render(request, 'main/add_trip.html', {'form': form})


def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    images = TripImage.objects.filter(trip=trip)
    return render(request, 'main/trip_detail.html', {
        'trip': trip,
        'images': images,
    })


# ===================================================================
# 🔑 FORGOT PASSWORD (OTP FLOW)
# ===================================================================

def forgot_password(request):
    """Send OTP to user's email"""
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "No account found with this email.")
                return redirect('forgot_password')

            otp = get_random_string(length=6, allowed_chars='0123456789')
            PasswordResetOTP.objects.create(user=user, otp=otp)

            send_mail(
                subject="Your Travel Tribe Password Reset OTP",
                message=f"Your OTP is {otp}. It will expire in 5 minutes.",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email],
            )

            request.session['reset_email'] = email
            messages.success(request, "OTP sent to your email.")
            return redirect('verify_otp')
    else:
        form = ForgotPasswordForm()
    return render(request, 'main/forgot_password.html', {'form': form})


def verify_otp(request):
    """Verify OTP and reset password"""
    email = request.session.get('reset_email')
    if not email:
        messages.error(request, "Session expired. Please try again.")
        return redirect('forgot_password')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('forgot_password')

    if request.method == 'POST':
        form = OTPVerifyForm(request.POST)
        if form.is_valid():
            otp_entered = form.cleaned_data['otp']
            new_password = form.cleaned_data['new_password']

            try:
                otp_record = PasswordResetOTP.objects.filter(user=user).latest('created_at')
            except PasswordResetOTP.DoesNotExist:
                messages.error(request, "OTP not found.")
                return redirect('forgot_password')

            if not otp_record.is_valid():
                messages.error(request, "OTP expired. Please request a new one.")
                return redirect('forgot_password')

            if otp_record.otp == otp_entered:
                user.set_password(new_password)
                user.save()
                PasswordResetOTP.objects.filter(user=user).delete()
                messages.success(request, "Password reset successful! You can log in now.")
                return redirect('login')
            else:
                messages.error(request, "Invalid OTP. Try again.")
    else:
        form = OTPVerifyForm()

    return render(request, 'main/verify_otp.html', {'form': form})


# ===================================================================
# 💡 TRIBE CONNECTION FEATURES
# ===================================================================

@login_required
def create_trip_post(request):
    if request.method == 'POST':
        form = TripPostForm(request.POST)
        if form.is_valid():
            trip_post = form.save(commit=False)
            trip_post.user = request.user
            trip_post.save()
            messages.success(request, "Trip post created successfully!")
            return redirect('trip_feed')
    else:
        form = TripPostForm()
    return render(request, 'main/create_trip.html', {'form': form})


@login_required
def trip_feed(request):
    """Display all trip posts with search and filter functionality"""
    trips = TripPost.objects.all()
    
    # Search by destination
    search_query = request.GET.get('search', '').strip()
    if search_query:
        trips = trips.filter(destination__icontains=search_query)
    
    # Filter by interests
    interest_filter = request.GET.get('interests', '')
    if interest_filter:
        trips = trips.filter(interests=interest_filter)
    
    # Filter by gender preference
    gender_filter = request.GET.get('gender', '')
    if gender_filter:
        trips = trips.filter(gender_preference=gender_filter)
    
    # Filter by date range
    start_date = request.GET.get('search_date', '')
    if start_date:
        trips = trips.filter(start_date__gte=start_date)
    
    # Filter by availability (not full)
    available_only = request.GET.get('available', '')
    if available_only == 'true':
        # Get trips where joined members count is less than limit
        from django.db.models import Count, F
        trips = trips.annotate(member_count=Count('joined_members')).filter(member_count__lt=F('members_limit'))
    
    trips = trips.order_by('-created_at')
    
    # Get filter choices for the form
    interest_choices = TripPost.INTEREST_CHOICES
    gender_choices = TripPost.GENDER_CHOICES
    
    context = {
        'trips': trips,
        'search_query': search_query,
        'interest_filter': interest_filter,
        'gender_filter': gender_filter,
        'available_only': available_only,
        'interest_choices': interest_choices,
        'gender_choices': gender_choices,
    }
    
    return render(request, 'main/trip_feed.html', context)


@login_required
def join_trip(request, trip_id):
    trip = get_object_or_404(TripPost, id=trip_id)
    
    # Check if user is already a member
    if request.user in trip.joined_members.all():
        messages.info(request, "You already joined this trip.")
        return redirect('trip_feed')
    
    # Check if trip is full
    if trip.members_count >= trip.members_limit:
        messages.warning(request, "This trip is already full.")
        return redirect('trip_feed')
    
    # Add user to trip
    trip.joined_members.add(request.user)
    messages.success(request, f"You joined {trip.destination} trip! You can now access the chat.")
    return redirect('trip_feed')


# ===================================================================
# 💬 CHATROOM (For Joined Tribe Members)
# ===================================================================

@login_required
def chat_room(request, trip_id):
    trip_post = get_object_or_404(TripPost, id=trip_id)
    chat_room_obj, created = ChatRoom.objects.get_or_create(trip_post=trip_post)
    chat_messages = ChatMessage.objects.filter(chat_room=chat_room_obj).order_by('timestamp')

    if request.user != trip_post.user and request.user not in trip_post.joined_members.all():
        messages.error(request, "You’re not part of this tribe.")
        return redirect('trip_feed')

    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        media_file = request.FILES.get('media_file')
        
        # Create message if there's content or media
        if content or media_file:
            ChatMessage.objects.create(
                chat_room=chat_room_obj, 
                user=request.user, 
                content=content,
                media_file=media_file
            )
            messages.success(request, "Message sent!")
        return redirect('chat_room', trip_id=trip_post.id)

    return render(request, 'main/chat.html', {'trip': trip_post, 'messages': chat_messages})



# ===================================================================
# ✏️ EDIT & DELETE TRIP POSTS
# ===================================================================

@login_required
def edit_trip_post(request, trip_id):
    """Allow users to edit their own trip posts"""
    trip_post = get_object_or_404(TripPost, id=trip_id)
    
    # Only the creator can edit
    if trip_post.user != request.user:
        messages.error(request, "You can only edit your own trips.")
        return redirect('trip_feed')
    
    if request.method == 'POST':
        form = TripPostForm(request.POST, instance=trip_post)
        if form.is_valid():
            form.save()
            messages.success(request, "Trip updated successfully!")
            return redirect('trip_feed')
    else:
        form = TripPostForm(instance=trip_post)
    
    return render(request, 'main/edit_trip.html', {'form': form, 'trip': trip_post})


@login_required
def delete_trip_post(request, trip_id):
    """Allow users to delete their own trip posts"""
    trip_post = get_object_or_404(TripPost, id=trip_id)
    
    # Only the creator can delete
    if trip_post.user != request.user:
        messages.error(request, "You can only delete your own trips.")
        return redirect('trip_feed')
    
    if request.method == 'POST':
        trip_post.delete()
        messages.success(request, "Trip deleted successfully!")
        return redirect('trip_feed')
    
    return render(request, 'main/confirm_delete.html', {'trip': trip_post})


@login_required
def leave_trip(request, trip_id):
    """Allow users to leave a trip they've joined"""
    trip = get_object_or_404(TripPost, id=trip_id)
    
    if request.user in trip.joined_members.all():
        trip.joined_members.remove(request.user)
        messages.success(request, f"You left {trip.destination} trip.")
    else:
        messages.info(request, "You're not part of this trip.")
    
    return redirect('trip_feed')



# ===================================================================
# 👤 USER PROFILE
# ===================================================================

@login_required
def user_profile(request):
    """View and edit user profile"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'main/profile.html', {'form': form, 'profile': profile})


# ===================================================================
# 🎯 JOIN/LEAVE DESTINATION TRIPS (Home Page Trips)
# ===================================================================

@login_required
def join_destination_trip(request, trip_id):
    """Allow users to join destination trips from home page"""
    trip = get_object_or_404(Trip, id=trip_id)
    
    # Check if user is already a member
    if request.user in trip.joined_members.all():
        messages.info(request, "You already joined this trip.")
        return redirect('trip_detail', trip_id=trip.id)
    
    # Check if trip is full
    if trip.is_full():
        messages.warning(request, "This trip is already full.")
        return redirect('trip_detail', trip_id=trip.id)
    
    # Add user to trip
    trip.joined_members.add(request.user)
    messages.success(request, f"You joined {trip.destination} trip!")
    return redirect('trip_detail', trip_id=trip.id)


@login_required
def leave_destination_trip(request, trip_id):
    """Allow users to leave destination trips"""
    trip = get_object_or_404(Trip, id=trip_id)
    
    if request.user in trip.joined_members.all():
        trip.joined_members.remove(request.user)
        messages.success(request, f"You left {trip.destination} trip.")
    else:
        messages.info(request, "You're not part of this trip.")
    
    return redirect('trip_detail', trip_id=trip.id)
