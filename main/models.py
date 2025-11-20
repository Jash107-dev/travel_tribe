# ==========================
# main/models.py
# ==========================
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

# ------------------------------------------------
# 🏕️ Trip Model (Main App Data)
# ------------------------------------------------
class Trip(models.Model):
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    tribe_count = models.PositiveIntegerField(default=1)

    FOOD_TYPE_CHOICES = [
        ('Veg', 'Veg'),
        ('Non-Veg', 'Non-Veg'),
        ('Both', 'Both'),
    ]
    food_type = models.CharField(max_length=10, choices=FOOD_TYPE_CHOICES, default='Both')

    CATEGORY_CHOICES = [
        ('Within Country', 'Within Country'),
        ('Outside Country', 'Outside Country'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='Within Country')

    description = models.TextField(blank=True, help_text="Short overview about this trip.")
    main_image = models.ImageField(upload_to='trip_images/', blank=True, null=True, help_text="Main image for the trip.")
    transport_modes = models.CharField(
        max_length=200,
        blank=True,
        help_text="Available transport options (e.g., Train, Flight, Bus, Car)."
    )
    must_visit_places = models.TextField(blank=True, help_text="Comma-separated list of must-visit places.")
    must_try_foods = models.TextField(blank=True, help_text="Comma-separated list of must-try local foods.")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # New fields for joining trips
    members_limit = models.PositiveIntegerField(default=10, help_text="Maximum number of members")
    joined_members = models.ManyToManyField(User, related_name='joined_destination_trips', blank=True)

    def __str__(self):
        return f"{self.destination} ({self.start_date} - {self.end_date})"
    
    @property
    def members_count(self):
        return self.joined_members.count()
    
    @property
    def is_full(self):
        return self.members_count >= self.members_limit
    
    def add_member_safely(self, user):
        """Only add member if they have an approved join request"""
        try:
            join_request = JoinRequest.objects.get(trip=self, user=user, status='approved')
            self.joined_members.add(user)
            return True
        except JoinRequest.DoesNotExist:
            print(f"WARNING: Attempted to add {user.username} to {self.destination} without approved request!")
            return False
    
    def save(self, *args, **kwargs):
        """Override save to prevent unauthorized member additions"""
        # Store original members before save
        if self.pk:
            original_members = set(self.joined_members.all())
        else:
            original_members = set()
        
        super().save(*args, **kwargs)
        
        # Check if any unauthorized members were added
        if self.pk:
            current_members = set(self.joined_members.all())
            new_members = current_members - original_members
            
            for member in new_members:
                if member != self.created_by:  # Allow trip creator
                    # Check if they have approved request
                    try:
                        JoinRequest.objects.get(trip=self, user=member, status='approved')
                    except JoinRequest.DoesNotExist:
                        # Remove unauthorized member
                        self.joined_members.remove(member)
                        print(f"🚫 BLOCKED: Removed {member.username} from {self.destination} - no approved request!")


# ------------------------------------------------
# 🔔 Join Request Model (Trip Approval System)
# ------------------------------------------------
class JoinRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='join_requests')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trip_join_requests')
    message = models.TextField(blank=True, help_text="Optional message to trip creator")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('trip', 'user')  # One request per user per trip
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username} → {self.trip.destination} ({self.status})"
    
    def approve(self):
        """ONLY WAY TO JOIN A TRIP - Approve the join request and add user to trip"""
        if self.status != 'pending':
            return False
            
        self.status = 'approved'
        self.save()
        
        # Add user to trip (ONLY place this should happen)
        self.trip.joined_members.add(self.user)
        
        # Award points
        self.user.profile.add_points(30)
        
        print(f"✅ APPROVED: {self.user.username} joined {self.trip.destination}")
        return True
    
    def reject(self):
        """Reject the join request"""
        self.status = 'rejected'
        self.save()


# ------------------------------------------------
# 📸 Extra Images for Trip (Gallery Section)
# ------------------------------------------------
class TripImage(models.Model):
    trip = models.ForeignKey(Trip, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='trip_gallery/')
    caption = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"Image for {self.trip.destination}"


# ------------------------------------------------
# 👤 User Profile Model
# ------------------------------------------------
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    bio = models.TextField(blank=True, max_length=500)
    interests = models.CharField(max_length=200, blank=True, help_text="Comma-separated interests")
    zodiac_sign = models.CharField(max_length=20, blank=True)
    mobile_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    
    # Gamification fields
    points = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    badges = models.TextField(blank=True, help_text="Comma-separated badge names")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
    @property
    def trips_created_count(self):
        return self.user.trip_set.count()
    
    @property
    def trips_joined_count(self):
        return self.user.joined_destination_trips.count() + self.user.joined_trips.count()
    
    @property
    def total_trips(self):
        return self.trips_created_count + self.trips_joined_count
    
    @property
    def badge_list(self):
        return [b.strip() for b in self.badges.split(',') if b.strip()]
    
    def add_points(self, points):
        """Add points and check for level up"""
        self.points += points
        # Level up every 100 points
        new_level = (self.points // 100) + 1
        if new_level > self.level:
            self.level = new_level
        self.save()
    
    def add_badge(self, badge_name):
        """Add a badge if not already earned"""
        badges = self.badge_list
        if badge_name not in badges:
            badges.append(badge_name)
            self.badges = ', '.join(badges)
            self.save()
            return True
        return False


# ------------------------------------------------
# 🔑 OTP Model (For Forgot Password Feature)
# ------------------------------------------------
class PasswordResetOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        """Check if OTP is still valid (within 5 minutes)."""
        return timezone.now() - self.created_at < timedelta(minutes=5)

    def __str__(self):
        return f"OTP for {self.user.username}"


# ------------------------------------------------
# 🌍 TripPost (Looking for Tribe Feature)
# ------------------------------------------------
class TripPost(models.Model):
    INTEREST_CHOICES = [
        ('Adventure', 'Adventure'),
        ('Relaxation', 'Relaxation'),
        ('Food', 'Food'),
        ('Culture', 'Culture'),
        ('Photography', 'Photography'),
        ('Friends', 'Friends'),
        ('Solo', 'Solo'),
    ]

    GENDER_CHOICES = [
        ('Any', 'Any'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trip_posts')
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    interests = models.CharField(max_length=100, choices=INTEREST_CHOICES)
    gender_preference = models.CharField(max_length=20, choices=GENDER_CHOICES, default='Any')
    budget_range = models.CharField(max_length=50, blank=True, null=True)
    members_limit = models.PositiveIntegerField(default=5)
    joined_members = models.ManyToManyField(User, related_name='joined_trips', blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s trip to {self.destination}"

    @property
    def members_count(self):
        return self.joined_members.count()

    class Meta:
        ordering = ['-created_at']


# ------------------------------------------------
# 💬 ChatRoom (For Both TripPost and Trip)
# ------------------------------------------------
class ChatRoom(models.Model):
    trip_post = models.OneToOneField(TripPost, on_delete=models.CASCADE, related_name='chatroom', null=True, blank=True)
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE, related_name='chatroom', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.trip_post:
            return f"ChatRoom for TripPost: {self.trip_post.destination}"
        elif self.trip:
            return f"ChatRoom for Trip: {self.trip.destination}"
        return "ChatRoom"
    
    @property
    def destination(self):
        if self.trip_post:
            return self.trip_post.destination
        elif self.trip:
            return self.trip.destination
        return "Unknown"


class ChatMessage(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    media_file = models.FileField(upload_to='chat_media/', blank=True, null=True, help_text="Upload image or video")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.content[:20] if self.content else '[Media]'}"
    
    def is_image(self):
        if self.media_file:
            return self.media_file.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))
        return False
    
    def is_video(self):
        if self.media_file:
            return self.media_file.name.lower().endswith(('.mp4', '.webm', '.ogg', '.mov'))
        return False

    class Meta:
        ordering = ['timestamp']


# ------------------------------------------------
# 🚀 Auto-create ChatRoom when TripPost or Trip is created
# ------------------------------------------------
@receiver(post_save, sender=TripPost)
def create_chatroom_for_trip_post(sender, instance, created, **kwargs):
    if created:
        ChatRoom.objects.create(trip_post=instance)
        print(f"💬 ChatRoom created for TripPost: {instance.destination}")

@receiver(post_save, sender=Trip)
def create_chatroom_for_trip(sender, instance, created, **kwargs):
    if created:
        ChatRoom.objects.create(trip=instance)
        print(f"💬 ChatRoom created for Trip: {instance.destination}")


# ------------------------------------------------
# ⭐ Trip Review Model
# ------------------------------------------------
class TripReview(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], help_text="Rating from 1 to 5")
    review_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('trip', 'user')  # One review per user per trip
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.user.username}'s review of {self.trip.destination} - {self.rating}⭐"


# ------------------------------------------------
# 📸 Trip Photo Gallery
# ------------------------------------------------
class TripPhoto(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='photos')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='trip_photos/')
    caption = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"Photo by {self.user.username} for {self.trip.destination}"


# ------------------------------------------------
# 🏆 Achievement/Badge System
# ------------------------------------------------
class Achievement(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=50, default='🏆')
    points_required = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.icon} {self.name}"


# ------------------------------------------------
# 🚀 Auto-create UserProfile when a User is created
# ------------------------------------------------
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print(f"👤 Profile created for {instance.username}")


# ------------------------------------------------
# 🎯 Award points and badges for actions
# ------------------------------------------------
@receiver(post_save, sender=Trip)
def award_trip_creation(sender, instance, created, **kwargs):
    if created:
        profile = instance.created_by.profile
        profile.add_points(50)  # 50 points for creating a trip
        if profile.trips_created_count == 1:
            profile.add_badge('First Trip Creator 🎉')
        if profile.trips_created_count == 5:
            profile.add_badge('Trip Master 🗺️')
        if profile.trips_created_count == 10:
            profile.add_badge('Travel Legend 🌟')


@receiver(post_save, sender=TripReview)
def award_review_points(sender, instance, created, **kwargs):
    if created:
        profile = instance.user.profile
        profile.add_points(20)  # 20 points for writing a review
        review_count = TripReview.objects.filter(user=instance.user).count()
        if review_count == 1:
            profile.add_badge('First Reviewer ⭐')
        if review_count == 10:
            profile.add_badge('Review Expert 📝')


@receiver(post_save, sender=TripPhoto)
def award_photo_points(sender, instance, created, **kwargs):
    if created:
        profile = instance.user.profile
        profile.add_points(10)  # 10 points for uploading a photo
        photo_count = TripPhoto.objects.filter(user=instance.user).count()
        if photo_count == 1:
            profile.add_badge('First Photo 📸')
        if photo_count == 20:
            profile.add_badge('Photographer 📷')
        if photo_count == 50:
            profile.add_badge('Photo Master 🎨')
