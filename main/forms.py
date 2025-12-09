from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date, timedelta
import re
from .models import Trip, TripPost, UserProfile

# ------------------------------------------------
# 🖼️ Multiple File Input Widget
# ------------------------------------------------
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

# ------------------------------------------------
# 🏕️ Trip Form (includes image, transport, places, foods)
# ------------------------------------------------
class TripForm(forms.ModelForm):
    # Multiple image upload field
    additional_images = MultipleFileField(
        required=False,
        label='Additional Images',
        help_text='You can select multiple images'
    )
    
    class Meta:
        model = Trip
        fields = [
            'destination', 'start_date', 'end_date', 'tribe_count', 
            'food_type', 'category', 'description', 'main_image', 
            'transport_modes', 'must_visit_places', 'must_try_foods',
            'members_limit'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Short overview about this trip'}),
            'transport_modes': forms.TextInput(attrs={'placeholder': 'Ex: Train, Flight, Car'}),
            'must_visit_places': forms.TextInput(attrs={'placeholder': 'Comma-separated must-visit places'}),
            'must_try_foods': forms.TextInput(attrs={'placeholder': 'Comma-separated must-try foods'}),
        }
    
    def clean_destination(self):
        destination = self.cleaned_data.get('destination')
        if not destination:
            raise ValidationError("Destination is required.")
        if len(destination.strip()) < 2:
            raise ValidationError("Destination must be at least 2 characters long.")
        if not re.match(r'^[a-zA-Z\s,.-]+$', destination):
            raise ValidationError("Destination can only contain letters, spaces, commas, periods, and hyphens.")
        return destination.strip().title()
    
    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if not start_date:
            raise ValidationError("Start date is required.")
        if start_date < date.today():
            raise ValidationError("Start date cannot be in the past.")
        if start_date > date.today() + timedelta(days=365):
            raise ValidationError("Start date cannot be more than 1 year in the future.")
        return start_date
    
    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        start_date = self.cleaned_data.get('start_date')
        
        if not end_date:
            raise ValidationError("End date is required.")
        if end_date < date.today():
            raise ValidationError("End date cannot be in the past.")
        if start_date and end_date <= start_date:
            raise ValidationError("End date must be after start date.")
        if start_date and (end_date - start_date).days > 365:
            raise ValidationError("Trip duration cannot exceed 1 year.")
        return end_date
    
    def clean_tribe_count(self):
        tribe_count = self.cleaned_data.get('tribe_count')
        if tribe_count is not None and tribe_count < 1:
            raise ValidationError("Tribe count must be at least 1.")
        if tribe_count is not None and tribe_count > 100:
            raise ValidationError("Tribe count cannot exceed 100.")
        return tribe_count
    
    def clean_members_limit(self):
        members_limit = self.cleaned_data.get('members_limit')
        if members_limit is not None and members_limit < 2:
            raise ValidationError("Members limit must be at least 2.")
        if members_limit is not None and members_limit > 50:
            raise ValidationError("Members limit cannot exceed 50.")
        return members_limit
    
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if description and len(description.strip()) < 10:
            raise ValidationError("Description must be at least 10 characters long.")
        if description and len(description) > 1000:
            raise ValidationError("Description cannot exceed 1000 characters.")
        return description.strip() if description else description

# ------------------------------------------------
# 👤 User Registration Form
# ------------------------------------------------
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        
        # Simple validation - just minimum length
        if len(password) < 5:
            raise forms.ValidationError("Password must be at least 5 characters long.")
        
        return password





# ------------------------------------------------
# 🌍 TripPost Form (Looking for Tribe)
# ------------------------------------------------
class TripPostForm(forms.ModelForm):
    class Meta:
        model = TripPost
        fields = [
            'destination', 'start_date', 'end_date', 'interests',
            'gender_preference', 'budget_range', 'members_limit', 'description'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['destination'].widget.attrs.update({'placeholder': 'Enter destination'})
        self.fields['budget_range'].widget.attrs.update({'placeholder': 'Ex: ₹5000 - ₹10000'})
        self.fields['gender_preference'].widget.attrs.update({'placeholder': 'Optional (e.g., Female Only)'})
        self.fields['description'].widget.attrs.update({'placeholder': 'Describe your travel interests...'})
    
    def clean_destination(self):
        destination = self.cleaned_data.get('destination')
        if not destination:
            raise ValidationError("Destination is required.")
        if len(destination.strip()) < 2:
            raise ValidationError("Destination must be at least 2 characters long.")
        if not re.match(r'^[a-zA-Z\s,.-]+$', destination):
            raise ValidationError("Destination can only contain letters, spaces, commas, periods, and hyphens.")
        return destination.strip().title()
    
    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if not start_date:
            raise ValidationError("Start date is required.")
        if start_date < date.today():
            raise ValidationError("Start date cannot be in the past.")
        return start_date
    
    def clean_end_date(self):
        end_date = self.cleaned_data.get('end_date')
        start_date = self.cleaned_data.get('start_date')
        
        if not end_date:
            raise ValidationError("End date is required.")
        if end_date < date.today():
            raise ValidationError("End date cannot be in the past.")
        if start_date and end_date <= start_date:
            raise ValidationError("End date must be after start date.")
        return end_date
    
    def clean_budget_range(self):
        budget_range = self.cleaned_data.get('budget_range')
        if budget_range and not re.match(r'^₹?\d+\s*-\s*₹?\d+$', budget_range.strip()):
            raise ValidationError("Budget range must be in format: ₹5000 - ₹10000")
        return budget_range.strip() if budget_range else budget_range
    
    def clean_members_limit(self):
        members_limit = self.cleaned_data.get('members_limit')
        if members_limit is not None and members_limit < 2:
            raise ValidationError("Members limit must be at least 2.")
        if members_limit is not None and members_limit > 20:
            raise ValidationError("Members limit cannot exceed 20.")
        return members_limit


# ------------------------------------------------
# 👤 User Profile Form
# ------------------------------------------------
class UserProfileForm(forms.ModelForm):
    ZODIAC_CHOICES = [
        ('', 'Select Zodiac Sign'),
        ('Aries', 'Aries ♈'),
        ('Taurus', 'Taurus ♉'),
        ('Gemini', 'Gemini ♊'),
        ('Cancer', 'Cancer ♋'),
        ('Leo', 'Leo ♌'),
        ('Virgo', 'Virgo ♍'),
        ('Libra', 'Libra ♎'),
        ('Scorpio', 'Scorpio ♏'),
        ('Sagittarius', 'Sagittarius ♐'),
        ('Capricorn', 'Capricorn ♑'),
        ('Aquarius', 'Aquarius ♒'),
        ('Pisces', 'Pisces ♓'),
    ]
    
    zodiac_sign = forms.ChoiceField(choices=ZODIAC_CHOICES, required=False)
    
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'interests', 'zodiac_sign', 'mobile_number', 'date_of_birth', 'location']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about yourself...'}),
            'interests': forms.TextInput(attrs={'placeholder': 'e.g., Hiking, Photography, Food'}),
            'mobile_number': forms.TextInput(attrs={'placeholder': '+91 1234567890'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'location': forms.TextInput(attrs={'placeholder': 'City, Country'}),
        }
    
    def clean_mobile_number(self):
        mobile_number = self.cleaned_data.get('mobile_number')
        if mobile_number:
            # Remove all non-digit characters except +
            cleaned = re.sub(r'[^\d+]', '', mobile_number)
            
            # Check for Indian mobile number format
            if cleaned.startswith('+91'):
                if len(cleaned) != 13:  # +91 + 10 digits
                    raise ValidationError("Indian mobile number must be 10 digits after +91")
                if not cleaned[3:].isdigit():
                    raise ValidationError("Mobile number must contain only digits after country code")
            elif cleaned.startswith('91') and len(cleaned) == 12:
                cleaned = '+' + cleaned  # Add + if missing
            elif len(cleaned) == 10 and cleaned.isdigit():
                cleaned = '+91' + cleaned  # Add +91 for Indian numbers
            else:
                raise ValidationError("Please enter a valid mobile number (10 digits for Indian numbers)")
            
            return cleaned
        return mobile_number
    
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            today = date.today()
            age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
            
            if date_of_birth >= today:
                raise ValidationError("Date of birth cannot be today or in the future")
            if age < 13:
                raise ValidationError("You must be at least 13 years old to use this platform")
            if age > 120:
                raise ValidationError("Please enter a valid date of birth")
        
        return date_of_birth
    
    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if bio and len(bio.strip()) < 10:
            raise ValidationError("Bio must be at least 10 characters long")
        if bio and len(bio) > 500:
            raise ValidationError("Bio cannot exceed 500 characters")
        return bio.strip() if bio else bio
    
    def clean_location(self):
        location = self.cleaned_data.get('location')
        if location and not re.match(r'^[a-zA-Z\s,.-]+$', location):
            raise ValidationError("Location can only contain letters, spaces, commas, periods, and hyphens")
        return location.strip().title() if location else location
