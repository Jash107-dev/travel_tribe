from django.urls import path
from . import simple_views

urlpatterns = [
    path('', simple_views.simple_home, name='home'),
    path('health/', simple_views.health_check, name='health'),
    path('test/', simple_views.simple_test, name='test'),
]