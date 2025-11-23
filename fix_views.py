#!/usr/bin/env python3
"""
Script to fix the syntax error in main/views.py
"""

def fix_views_file():
    with open('main/views_backup.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and replace the problematic function
    old_function = '''@login_required
def join_destination_trip(request, trip_id):
    """Simple direct join system"""
    try:
        trip = get_object_or_404(Trip, id=trip_id)
        
        # Basic checks
        if request.user == trip.created_by:
            messages.info(request, "You are the creator of this trip.")
            return redirect('trip_detail', trip_id=trip.id)
        
        if request.user in trip.joined_members.all():
            messages.info(request, "You are already a member of this trip.")
            return redirect('trip_detail', trip_id=trip.id)
        
        # Simple join
        trip.joined_members.add(request.user)
        messages.success(request, f"🎉 Welcome to {trip.destination}!")
        return redirect('trip_detail', trip_id=trip.id)
        
    except Exception as e:
        messages.error(request, f"Error joining trip: {str(e)}")
        return redirect('home')'''
    
    new_function = '''@login_required
def join_destination_trip(request, trip_id):
    """Simple direct join system"""
    trip = get_object_or_404(Trip, id=trip_id)
    
    # Basic checks
    if request.user == trip.created_by:
        messages.info(request, "You are the creator of this trip.")
        return redirect('trip_detail', trip_id=trip.id)
    
    if request.user in trip.joined_members.all():
        messages.info(request, "You are already a member of this trip.")
        return redirect('trip_detail', trip_id=trip.id)
    
    # Simple join
    trip.joined_members.add(request.user)
    messages.success(request, f"🎉 Welcome to {trip.destination}!")
    return redirect('trip_detail', trip_id=trip.id)'''
    
    # Replace the function
    content = content.replace(old_function, new_function)
    
    # Write the fixed content
    with open('main/views.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Fixed views.py successfully!")

if __name__ == '__main__':
    fix_views_file()