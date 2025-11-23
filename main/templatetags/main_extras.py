from django import template
import os

register = template.Library()

@register.filter
def safe_image_url(image_field):
    """Return image URL if file exists, otherwise return None"""
    if not image_field:
        return None
    
    try:
        # Check if file exists
        if hasattr(image_field, 'path') and os.path.exists(image_field.path):
            return image_field.url
        elif hasattr(image_field, 'url'):
            return image_field.url
    except (ValueError, AttributeError):
        pass
    
    return None

@register.filter
def has_valid_image(image_field):
    """Check if image field has a valid image"""
    if not image_field:
        return False
    
    try:
        # Check if file exists
        if hasattr(image_field, 'path'):
            return os.path.exists(image_field.path)
        return bool(image_field)
    except (ValueError, AttributeError):
        return False
