# travel_tribe/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin Interface
    path('admin/', admin.site.urls),

    # 1. User Authentication URLs (Django's built-in views)
    path('accounts/', include('django.contrib.auth.urls')),

    # 2. Main Application URLs
    path('', include('main.urls')),

    
]

# ✅ Serve media and static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
