from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    # Trips & Home
    path('home/', views.home, name='home'),
    path('add-trip/', views.add_trip, name='add_trip'),
    path('trip/<int:trip_id>/', views.trip_detail, name='trip_detail'),



    # Trip posts
    path('create-trip/', views.create_trip_post, name='create_trip'),
    path('trips/', views.trip_feed, name='trip_feed'),
    path('join-trip/<int:trip_id>/', views.join_trip, name='join_trip'),

    # Chat
    path('chat/<int:trip_id>/', views.chat_room, name='chat_room'),
    path('destination-chat/<int:trip_id>/', views.destination_chat_room, name='destination_chat_room'),
    
    # Edit/Delete Trip Posts
    path('edit-trip/<int:trip_id>/', views.edit_trip_post, name='edit_trip_post'),
    path('delete-trip/<int:trip_id>/', views.delete_trip_post, name='delete_trip_post'),
    path('leave-trip/<int:trip_id>/', views.leave_trip, name='leave_trip'),
    
    # User Profile
    path('profile/', views.user_profile, name='user_profile'),
    path('my-trips/', views.my_trips, name='my_trips'),
    
    # Join/Leave Destination Trips
    path('join-destination-trip/<int:trip_id>/', views.join_destination_trip, name='join_destination_trip'),
    path('leave-destination-trip/<int:trip_id>/', views.leave_destination_trip, name='leave_destination_trip'),
    

    
    # Real-time Chat API
    path('api/chat/<int:trip_id>/messages/', views.get_new_messages, name='get_new_messages'),

    
    # Reviews & Ratings
    path('trip/<int:trip_id>/review/', views.add_review, name='add_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    
    # Photo Gallery
    path('trip/<int:trip_id>/upload-photo/', views.upload_photo, name='upload_photo'),
    path('photo/<int:photo_id>/delete/', views.delete_photo, name='delete_photo'),
    

    path('profile/<str:username>/', views.public_profile, name='public_profile'),
    
    # Hunt & Chatbot
    path('hunt/', views.hunt_view, name='hunt'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
    
    # Admin user creation (for Render free tier)
    path('create-admin-user/', views.create_admin_user, name='create_admin_user'),
    
    # Health check
    path('health/', views.health_check, name='health_check'),
]
