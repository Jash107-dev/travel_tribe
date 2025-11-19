from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Trip, TripImage, PasswordResetOTP, TripPost, ChatRoom, ChatMessage, UserProfile, JoinRequest, TripReview
from .forms import TripForm, UserRegisterForm, ForgotPasswordForm, OTPVerifyForm, TripPostForm, UserProfileForm
from django.http import JsonResponse
from django.db import models

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
    
    # Get join request status for current user
    join_request_status = None
    pending_requests_count = 0
    
    if request.user.is_authenticated:
        # Check if user has a join request
        try:
            join_request = JoinRequest.objects.get(trip=trip, user=request.user)
            join_request_status = join_request.status
        except JoinRequest.DoesNotExist:
            join_request_status = None
        
        # Count pending requests if user is trip creator
        if request.user == trip.created_by:
            pending_requests_count = JoinRequest.objects.filter(trip=trip, status='pending').count()
    
    return render(request, 'main/trip_detail.html', {
        'trip': trip,
        'images': images,
        'join_request_status': join_request_status,
        'pending_requests_count': pending_requests_count,
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
    
    return redirect('my_trips')


@login_required
def my_trips(request):
    """View all trips the user has joined"""
    joined_trips = TripPost.objects.filter(joined_members=request.user).order_by('-created_at')
    created_trips = TripPost.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'joined_trips': joined_trips,
        'created_trips': created_trips,
    }
    return render(request, 'main/my_trips.html', context)



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
    """Send join request for destination trip"""
    trip = get_object_or_404(Trip, id=trip_id)
    
    print(f"DEBUG: User {request.user.username} trying to join trip {trip.destination}")
    print(f"DEBUG: Request method: {request.method}")
    
    # Check if user is the trip creator
    if request.user == trip.created_by:
        messages.info(request, "You are the creator of this trip.")
        return redirect('trip_detail', trip_id=trip.id)
    
    # Check if user is already a member
    if request.user in trip.joined_members.all():
        messages.info(request, "You already joined this trip.")
        return redirect('trip_detail', trip_id=trip.id)
    
    # Check if trip is full
    if trip.is_full():
        messages.warning(request, "This trip is already full.")
        return redirect('trip_detail', trip_id=trip.id)
    
    # Check if request already exists
    from main.models import JoinRequest
    existing_request = JoinRequest.objects.filter(trip=trip, user=request.user).first()
    
    if existing_request:
        if existing_request.status == 'pending':
            messages.info(request, "Your join request is pending approval.")
        elif existing_request.status == 'rejected':
            messages.warning(request, "Your previous request was rejected.")
        return redirect('trip_detail', trip_id=trip.id)
    
    # Create join request
    if request.method == 'POST':
        message = request.POST.get('message', '')
        JoinRequest.objects.create(
            trip=trip,
            user=request.user,
            message=message
        )
        messages.success(request, f"Join request sent to {trip.created_by.username}!")
        return redirect('trip_detail', trip_id=trip.id)
    
    # Show request form
    return render(request, 'main/join_request_form.html', {'trip': trip})


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


@login_required
def manage_join_requests(request, trip_id):
    """View and manage join requests for a trip (creator only)"""
    from main.models import JoinRequest
    trip = get_object_or_404(Trip, id=trip_id)
    
    # Only trip creator can manage requests
    if request.user != trip.created_by:
        messages.error(request, "Only the trip creator can manage join requests.")
        return redirect('trip_detail', trip_id=trip.id)
    
    pending_requests = JoinRequest.objects.filter(trip=trip, status='pending')
    approved_requests = JoinRequest.objects.filter(trip=trip, status='approved')
    rejected_requests = JoinRequest.objects.filter(trip=trip, status='rejected')
    
    context = {
        'trip': trip,
        'pending_requests': pending_requests,
        'approved_requests': approved_requests,
        'rejected_requests': rejected_requests,
    }
    return render(request, 'main/manage_requests.html', context)


@login_required
def approve_join_request(request, request_id):
    """Approve a join request"""
    from main.models import JoinRequest
    join_request = get_object_or_404(JoinRequest, id=request_id)
    
    # Only trip creator can approve
    if request.user != join_request.trip.created_by:
        messages.error(request, "You don't have permission to approve this request.")
        return redirect('home')
    
    # Check if trip is full
    if join_request.trip.is_full():
        messages.warning(request, "Trip is full. Cannot approve more members.")
        return redirect('manage_join_requests', trip_id=join_request.trip.id)
    
    join_request.approve()
    messages.success(request, f"Approved {join_request.user.username}'s request!")
    return redirect('manage_join_requests', trip_id=join_request.trip.id)


@login_required
def reject_join_request(request, request_id):
    """Reject a join request"""
    from main.models import JoinRequest
    join_request = get_object_or_404(JoinRequest, id=request_id)
    
    # Only trip creator can reject
    if request.user != join_request.trip.created_by:
        messages.error(request, "You don't have permission to reject this request.")
        return redirect('home')
    
    join_request.reject()
    messages.success(request, f"Rejected {join_request.user.username}'s request.")
    return redirect('manage_join_requests', trip_id=join_request.trip.id)


@login_required
def view_requester_profile(request, user_id):
    """View profile of user who requested to join"""
    user = get_object_or_404(User, id=user_id)
    profile = user.profile
    
    # Get user's trip history
    created_trips = Trip.objects.filter(created_by=user)
    joined_trips = user.joined_destination_trips.all()
    reviews = TripReview.objects.filter(user=user)
    
    context = {
        'profile_user': user,
        'profile': profile,
        'created_trips': created_trips,
        'joined_trips': joined_trips,
        'reviews': reviews,
    }
    return render(request, 'main/requester_profile.html', context)


# ===================================================================
# 📡 REAL-TIME CHAT API ENDPOINTS
# ===================================================================

@login_required
def get_new_messages(request, trip_id):
    """API endpoint to fetch new messages for real-time updates"""
    trip_post = get_object_or_404(TripPost, id=trip_id)
    
    # Check if user is part of the trip
    if request.user != trip_post.user and request.user not in trip_post.joined_members.all():
        return JsonResponse({'error': 'Unauthorized'}, status=403)
    
    # Get the last message ID from the request
    last_message_id = request.GET.get('last_id', 0)
    
    try:
        chat_room_obj = ChatRoom.objects.get(trip_post=trip_post)
        new_messages = ChatMessage.objects.filter(
            chat_room=chat_room_obj,
            id__gt=last_message_id
        ).order_by('timestamp')
        
        messages_data = []
        for msg in new_messages:
            messages_data.append({
                'id': msg.id,
                'user': msg.user.username,
                'user_id': msg.user.id,
                'content': msg.content,
                'timestamp': msg.timestamp.strftime('%b %d, %H:%M'),
                'is_image': msg.is_image(),
                'is_video': msg.is_video(),
                'media_url': msg.media_file.url if msg.media_file else None,
            })
        
        return JsonResponse({
            'messages': messages_data,
            'count': len(messages_data)
        })
    except ChatRoom.DoesNotExist:
        return JsonResponse({'messages': [], 'count': 0})


@login_required
def get_unread_count(request):
    """API endpoint to get unread message count across all trips"""
    # Get all trips the user is part of
    user_trips = TripPost.objects.filter(
        models.Q(user=request.user) | models.Q(joined_members=request.user)
    ).distinct()
    
    # Get the last seen message ID for each trip from session
    last_seen = request.session.get('last_seen_messages', {})
    
    total_unread = 0
    trip_unread = {}
    
    for trip in user_trips:
        try:
            chat_room_obj = ChatRoom.objects.get(trip_post=trip)
            last_seen_id = last_seen.get(str(trip.id), 0)
            
            # Count messages after last seen that are not from current user
            unread = ChatMessage.objects.filter(
                chat_room=chat_room_obj,
                id__gt=last_seen_id
            ).exclude(user=request.user).count()
            
            if unread > 0:
                trip_unread[trip.id] = {
                    'count': unread,
                    'destination': trip.destination
                }
                total_unread += unread
        except ChatRoom.DoesNotExist:
            continue
    
    return JsonResponse({
        'total_unread': total_unread,
        'trips': trip_unread
    })


@login_required
def mark_messages_read(request, trip_id):
    """Mark messages as read for a specific trip"""
    if request.method == 'POST':
        trip_post = get_object_or_404(TripPost, id=trip_id)
        
        # Check if user is part of the trip
        if request.user != trip_post.user and request.user not in trip_post.joined_members.all():
            return JsonResponse({'error': 'Unauthorized'}, status=403)
        
        try:
            chat_room_obj = ChatRoom.objects.get(trip_post=trip_post)
            last_message = ChatMessage.objects.filter(chat_room=chat_room_obj).order_by('-id').first()
            
            if last_message:
                # Store last seen message ID in session
                last_seen = request.session.get('last_seen_messages', {})
                last_seen[str(trip_id)] = last_message.id
                request.session['last_seen_messages'] = last_seen
                request.session.modified = True
                
                return JsonResponse({'success': True, 'last_id': last_message.id})
        except ChatRoom.DoesNotExist:
            pass
    
    return JsonResponse({'success': False})


# ===================================================================
# ⭐ TRIP REVIEWS & RATINGS
# ===================================================================

@login_required
def add_review(request, trip_id):
    """Add a review for a trip"""
    from .models import TripReview
    trip = get_object_or_404(Trip, id=trip_id)
    
    # Check if user has already reviewed this trip
    existing_review = TripReview.objects.filter(trip=trip, user=request.user).first()
    
    if request.method == 'POST':
        rating = request.POST.get('rating')
        review_text = request.POST.get('review_text', '').strip()
        
        if not rating:
            messages.error(request, "Please select a rating.")
            return redirect('trip_detail', trip_id=trip.id)
        
        if existing_review:
            # Update existing review
            existing_review.rating = int(rating)
            existing_review.review_text = review_text
            existing_review.save()
            messages.success(request, "Review updated successfully!")
        else:
            # Create new review
            TripReview.objects.create(
                trip=trip,
                user=request.user,
                rating=int(rating),
                review_text=review_text
            )
            messages.success(request, "Review added successfully! You earned 20 points! ⭐")
        
        return redirect('trip_detail', trip_id=trip.id)
    
    return redirect('trip_detail', trip_id=trip.id)


@login_required
def delete_review(request, review_id):
    """Delete a review"""
    from .models import TripReview
    review = get_object_or_404(TripReview, id=review_id)
    
    if review.user != request.user:
        messages.error(request, "You can only delete your own reviews.")
        return redirect('trip_detail', trip_id=review.trip.id)
    
    trip_id = review.trip.id
    review.delete()
    messages.success(request, "Review deleted successfully!")
    return redirect('trip_detail', trip_id=trip_id)


# ===================================================================
# 📸 TRIP PHOTO GALLERY
# ===================================================================

@login_required
def upload_photo(request, trip_id):
    """Upload a photo to a trip"""
    from .models import TripPhoto
    trip = get_object_or_404(Trip, id=trip_id)
    
    if request.method == 'POST':
        photo = request.FILES.get('photo')
        caption = request.POST.get('caption', '').strip()
        
        if not photo:
            messages.error(request, "Please select a photo to upload.")
            return redirect('trip_detail', trip_id=trip.id)
        
        TripPhoto.objects.create(
            trip=trip,
            user=request.user,
            photo=photo,
            caption=caption
        )
        messages.success(request, "Photo uploaded successfully! You earned 10 points! 📸")
        return redirect('trip_detail', trip_id=trip.id)
    
    return redirect('trip_detail', trip_id=trip.id)


@login_required
def delete_photo(request, photo_id):
    """Delete a photo"""
    from .models import TripPhoto
    photo = get_object_or_404(TripPhoto, id=photo_id)
    
    if photo.user != request.user:
        messages.error(request, "You can only delete your own photos.")
        return redirect('trip_detail', trip_id=photo.trip.id)
    
    trip_id = photo.trip.id
    photo.delete()
    messages.success(request, "Photo deleted successfully!")
    return redirect('trip_detail', trip_id=trip_id)


# ===================================================================
# 🏆 GAMIFICATION - LEADERBOARD & ACHIEVEMENTS
# ===================================================================

def leaderboard(request):
    """Display leaderboard with top users by points"""
    top_users = UserProfile.objects.all().order_by('-points', '-level')[:50]
    
    # Get current user's rank if logged in
    user_rank = None
    if request.user.is_authenticated:
        user_profile = request.user.profile
        user_rank = UserProfile.objects.filter(points__gt=user_profile.points).count() + 1
    
    context = {
        'top_users': top_users,
        'user_rank': user_rank,
    }
    return render(request, 'main/leaderboard.html', context)


@login_required
def achievements(request):
    """Display user's achievements and badges"""
    profile = request.user.profile
    
    # Define all possible achievements
    all_achievements = [
        {'name': 'First Trip Creator 🎉', 'description': 'Create your first trip', 'earned': 'First Trip Creator 🎉' in profile.badge_list},
        {'name': 'Trip Master 🗺️', 'description': 'Create 5 trips', 'earned': 'Trip Master 🗺️' in profile.badge_list},
        {'name': 'Travel Legend 🌟', 'description': 'Create 10 trips', 'earned': 'Travel Legend 🌟' in profile.badge_list},
        {'name': 'First Reviewer ⭐', 'description': 'Write your first review', 'earned': 'First Reviewer ⭐' in profile.badge_list},
        {'name': 'Review Expert 📝', 'description': 'Write 10 reviews', 'earned': 'Review Expert 📝' in profile.badge_list},
        {'name': 'First Photo 📸', 'description': 'Upload your first photo', 'earned': 'First Photo 📸' in profile.badge_list},
        {'name': 'Photographer 📷', 'description': 'Upload 20 photos', 'earned': 'Photographer 📷' in profile.badge_list},
        {'name': 'Photo Master 🎨', 'description': 'Upload 50 photos', 'earned': 'Photo Master 🎨' in profile.badge_list},
    ]
    
    context = {
        'profile': profile,
        'all_achievements': all_achievements,
    }
    return render(request, 'main/achievements.html', context)


@login_required
def public_profile(request, username):
    """View another user's public profile"""
    user = get_object_or_404(User, username=username)
    profile = user.profile
    
    # Get user's trips and stats
    created_trips = Trip.objects.filter(created_by=user).order_by('-created_at')[:5]
    from .models import TripReview, TripPhoto
    recent_reviews = TripReview.objects.filter(user=user).order_by('-created_at')[:5]
    recent_photos = TripPhoto.objects.filter(user=user).order_by('-uploaded_at')[:6]
    
    context = {
        'profile_user': user,
        'profile': profile,
        'created_trips': created_trips,
        'recent_reviews': recent_reviews,
        'recent_photos': recent_photos,
    }
    return render(request, 'main/public_profile.html', context)


# ===================================================================
# 🔍 HUNT FEATURE (Search Destinations)
# ===================================================================

def hunt_view(request):
    """Hunt feature to search destinations"""
    return render(request, 'main/hunt.html')


# ===================================================================
# 🤖 CHATBOT FEATURE
# ===================================================================

def chatbot_view(request):
    """AI Travel Assistant Chatbot"""
    return render(request, 'main/chatbot.html')
