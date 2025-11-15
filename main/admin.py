from django.contrib import admin
from .models import Trip, TripImage, TripPost, ChatRoom, ChatMessage, PasswordResetOTP, UserProfile

# ================================================
# TRIP MANAGEMENT
# ================================================

class TripImageInline(admin.TabularInline):
    model = TripImage
    extra = 1
    fields = ('image', 'caption')

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('destination', 'start_date', 'end_date', 'category', 'members_count', 'members_limit', 'created_by', 'created_at')
    search_fields = ('destination', 'category', 'description')
    list_filter = ('category', 'food_type', 'start_date', 'created_at')
    date_hierarchy = 'start_date'
    inlines = [TripImageInline]
    readonly_fields = ('created_at',)
    filter_horizontal = ('joined_members',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('destination', 'category', 'start_date', 'end_date', 'members_limit')
        }),
        ('Details', {
            'fields': ('description', 'food_type', 'transport_modes')
        }),
        ('Recommendations', {
            'fields': ('must_visit_places', 'must_try_foods')
        }),
        ('Media', {
            'fields': ('main_image',)
        }),
        ('Members', {
            'fields': ('joined_members',),
            'description': 'Manage users who have joined this trip'
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    def members_count(self, obj):
        return obj.members_count
    members_count.short_description = 'Members'

@admin.register(TripImage)
class TripImageAdmin(admin.ModelAdmin):
    list_display = ('trip', 'caption', 'image')
    search_fields = ('trip__destination', 'caption')

# ================================================
# TRIP POSTS (TRIBE FINDER)
# ================================================

@admin.register(TripPost)
class TripPostAdmin(admin.ModelAdmin):
    list_display = ('destination', 'user', 'start_date', 'end_date', 'interests', 'members_count', 'members_limit', 'created_at')
    search_fields = ('destination', 'user__username', 'description')
    list_filter = ('interests', 'gender_preference', 'start_date', 'created_at')
    date_hierarchy = 'start_date'
    filter_horizontal = ('joined_members',)
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Trip Information', {
            'fields': ('user', 'destination', 'start_date', 'end_date')
        }),
        ('Preferences', {
            'fields': ('interests', 'gender_preference', 'budget_range', 'members_limit')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Members', {
            'fields': ('joined_members',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

# ================================================
# CHAT SYSTEM
# ================================================

class ChatMessageInline(admin.TabularInline):
    model = ChatMessage
    extra = 0
    fields = ('user', 'content', 'media_file', 'timestamp')
    readonly_fields = ('timestamp',)
    can_delete = True

@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('trip_post', 'created_at', 'message_count')
    search_fields = ('trip_post__destination',)
    readonly_fields = ('created_at',)
    inlines = [ChatMessageInline]
    
    def message_count(self, obj):
        return obj.messages.count()
    message_count.short_description = 'Messages'

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'chat_room', 'content_preview', 'has_media', 'timestamp')
    search_fields = ('user__username', 'content', 'chat_room__trip_post__destination')
    list_filter = ('timestamp',)
    date_hierarchy = 'timestamp'
    readonly_fields = ('timestamp',)
    
    def content_preview(self, obj):
        if obj.content:
            return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
        return '[Media Only]'
    content_preview.short_description = 'Content'
    
    def has_media(self, obj):
        return bool(obj.media_file)
    has_media.boolean = True
    has_media.short_description = 'Media'

# ================================================
# PASSWORD RESET
# ================================================

@admin.register(PasswordResetOTP)
class PasswordResetOTPAdmin(admin.ModelAdmin):
    list_display = ('user', 'otp', 'created_at', 'is_valid')
    search_fields = ('user__username', 'user__email')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    
    def is_valid(self, obj):
        return obj.is_valid()
    is_valid.boolean = True
    is_valid.short_description = 'Valid'


# ================================================
# USER PROFILE
# ================================================

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'zodiac_sign', 'location', 'mobile_number', 'created_at')
    search_fields = ('user__username', 'user__email', 'location', 'interests')
    list_filter = ('zodiac_sign', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('User', {
            'fields': ('user',)
        }),
        ('Profile Information', {
            'fields': ('profile_picture', 'bio', 'interests')
        }),
        ('Personal Details', {
            'fields': ('zodiac_sign', 'date_of_birth', 'mobile_number', 'location')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
