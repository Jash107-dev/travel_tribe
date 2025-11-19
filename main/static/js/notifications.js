// ===================================================================
// 🔔 GLOBAL NOTIFICATION SYSTEM FOR TRAVEL TRIBE
// ===================================================================

(function() {
    'use strict';
    
    let unreadCount = 0;
    let notificationBadge = null;
    
    // Initialize notification system
    function initNotifications() {
        // Request notification permission
        if ('Notification' in window && Notification.permission === 'default') {
            Notification.requestPermission();
        }
        
        // Create notification badge in navbar
        createNotificationBadge();
        
        // Start polling for unread messages
        startPolling();
    }
    
    // Create notification badge element
    function createNotificationBadge() {
        // Find the My Trips link or create a notification icon
        const navbar = document.querySelector('nav') || document.querySelector('.navbar') || document.querySelector('header');
        
        if (!navbar) return;
        
        // Create notification bell icon
        const notificationContainer = document.createElement('div');
        notificationContainer.className = 'notification-container';
        notificationContainer.style.cssText = 'position: relative; display: inline-block; margin: 0 15px;';
        
        const bellIcon = document.createElement('a');
        bellIcon.href = '/my-trips/';
        bellIcon.innerHTML = '<i class="fas fa-bell"></i>';
        bellIcon.style.cssText = 'color: #fff; font-size: 20px; text-decoration: none; position: relative;';
        bellIcon.title = 'Notifications';
        
        notificationBadge = document.createElement('span');
        notificationBadge.className = 'notification-badge';
        notificationBadge.style.cssText = `
            position: absolute;
            top: -8px;
            right: -8px;
            background: #ff4444;
            color: white;
            border-radius: 50%;
            padding: 2px 6px;
            font-size: 11px;
            font-weight: bold;
            display: none;
            min-width: 18px;
            text-align: center;
        `;
        
        bellIcon.appendChild(notificationBadge);
        notificationContainer.appendChild(bellIcon);
        
        // Try to insert near My Trips link
        const myTripsLink = Array.from(navbar.querySelectorAll('a')).find(a => 
            a.textContent.includes('My Trips') || a.href.includes('my-trips')
        );
        
        if (myTripsLink && myTripsLink.parentNode) {
            myTripsLink.parentNode.insertBefore(notificationContainer, myTripsLink);
        } else {
            // Fallback: append to navbar
            navbar.appendChild(notificationContainer);
        }
    }
    
    // Update notification badge
    function updateBadge(count) {
        unreadCount = count;
        
        if (notificationBadge) {
            if (count > 0) {
                notificationBadge.textContent = count > 99 ? '99+' : count;
                notificationBadge.style.display = 'block';
                
                // Update page title
                document.title = `(${count}) ${document.title.replace(/^\(\d+\)\s*/, '')}`;
            } else {
                notificationBadge.style.display = 'none';
                
                // Reset page title
                document.title = document.title.replace(/^\(\d+\)\s*/, '');
            }
        }
    }
    
    // Fetch unread message count
    async function fetchUnreadCount() {
        try {
            const response = await fetch('/api/notifications/unread/');
            const data = await response.json();
            
            if (data.total_unread !== unreadCount) {
                updateBadge(data.total_unread);
                
                // Show desktop notification if count increased
                if (data.total_unread > unreadCount && unreadCount > 0) {
                    showDesktopNotification(data);
                }
            }
        } catch (error) {
            console.error('Error fetching unread count:', error);
        }
    }
    
    // Show desktop notification
    function showDesktopNotification(data) {
        if ('Notification' in window && Notification.permission === 'granted') {
            const tripNames = Object.values(data.trips).map(t => t.destination).join(', ');
            const message = data.total_unread === 1 
                ? `You have 1 new message in ${tripNames}`
                : `You have ${data.total_unread} new messages`;
            
            const notification = new Notification('Travel Tribe', {
                body: message,
                icon: '/static/img/perry_chatbot.jpg',
                badge: '/static/img/perry_chatbot.jpg',
                tag: 'unread-messages',
                requireInteraction: false
            });
            
            notification.onclick = function() {
                window.location.href = '/my-trips/';
                notification.close();
            };
            
            setTimeout(() => notification.close(), 5000);
        }
    }
    
    // Start polling for notifications
    function startPolling() {
        // Initial fetch
        fetchUnreadCount();
        
        // Poll every 10 seconds
        setInterval(fetchUnreadCount, 10000);
        
        // Also fetch when page becomes visible
        document.addEventListener('visibilitychange', () => {
            if (!document.hidden) {
                fetchUnreadCount();
            }
        });
    }
    
    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initNotifications);
    } else {
        initNotifications();
    }
})();
