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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


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
# 💬 ChatRoom (Each TripPost Gets One Chat Room)
# ------------------------------------------------
class ChatRoom(models.Model):
    trip_post = models.OneToOneField(TripPost, on_delete=models.CASCADE, related_name='chatroom')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChatRoom for {self.trip_post.destination}"


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
# 🚀 Auto-create ChatRoom when a TripPost is created
# ------------------------------------------------
@receiver(post_save, sender=TripPost)
def create_chatroom_for_trip_post(sender, instance, created, **kwargs):
    if created:
        ChatRoom.objects.create(trip_post=instance)
        print(f"💬 ChatRoom created for {instance.destination}")


# ------------------------------------------------
# 🚀 Auto-create UserProfile when a User is created
# ------------------------------------------------
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print(f"👤 Profile created for {instance.username}")
