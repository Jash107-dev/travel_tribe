from django import template
from main.models import JoinRequest

register = template.Library()

@register.simple_tag
def get_pending_requests_count(trip):
    """Get count of pending join requests for a trip"""
    return JoinRequest.objects.filter(trip=trip, status='pending').count()

@register.simple_tag
def get_join_request_status(trip, user):
    """Get the status of a user's join request for a trip"""
    try:
        request = JoinRequest.objects.get(trip=trip, user=user)
        return request.status
    except JoinRequest.DoesNotExist:
        return None
