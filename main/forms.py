from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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

# ------------------------------------------------
# 👤 User Registration Form
# ------------------------------------------------
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
    
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        
        if len(password) < 5:
            raise forms.ValidationError("Password must be at least 5 characters long.")
        
        # Check for uppercase letter
        if not any(c.isupper() for c in password):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")
        
        # Check for lowercase letter
        if not any(c.islower() for c in password):
            raise forms.ValidationError("Password must contain at least one lowercase letter.")
        
        # Check for digit
        if not any(c.isdigit() for c in password):
            raise forms.ValidationError("Password must contain at least one number.")
        
        # Check for special character
        special_chars = "!@#$%^&*(),.?\":{}|<>"
        if not any(c in special_chars for c in password):
            raise forms.ValidationError("Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>).")
        
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# ------------------------------------------------
# 🔑 Forgot Password / OTP Forms
# ------------------------------------------------
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label="Registered Email")

class OTPVerifyForm(forms.Form):
    otp = forms.CharField(label="Enter OTP", max_length=6)
    new_password = forms.CharField(label="New Password", widget=forms.PasswordInput())

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
