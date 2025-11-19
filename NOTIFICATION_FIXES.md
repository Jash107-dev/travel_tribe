# Notification & Chat UI Fixes

## Issues Fixed

### 1. Notification Badge Not Clearing After Opening Chat
**Problem:** The notification badge (showing "5" etc.) remained visible even after opening the chat.

**Solution:**
- Added automatic badge refresh when chat page opens
- Chat page now calls `markAsRead()` immediately on load
- Badge updates every 10 seconds while chat is open
- Final badge refresh when leaving chat page
- Exposed `fetchUnreadCount()` globally so chat pages can trigger updates

**Files Modified:**
- `main/static/js/notifications.js` - Exposed fetchUnreadCount globally
- `main/templates/main/chat.html` - Added badge refresh triggers

### 2. Mobile Send Button Shrinking
**Problem:** On mobile devices, the send button was shrinking and hard to tap while chatting.

**Solution:**
- Added `flex-shrink: 0` to prevent button from shrinking
- Added `min-width` and `min-height` to maintain button size
- Applied to both desktop (50px) and mobile (45px) breakpoints
- Also applied to attachment icon button for consistency

**Files Modified:**
- `main/static/css/chat_modern.css` - Fixed button sizing

## Changes Summary

### CSS Changes (chat_modern.css)
```css
.send-btn {
  min-width: 50px;
  min-height: 50px;
  flex-shrink: 0;
  /* ... other styles ... */
}

.chat-footer .icon-btn {
  flex-shrink: 0;
  /* ... other styles ... */
}

@media (max-width: 768px) {
  .send-btn {
    min-width: 45px;
    min-height: 45px;
  }
}
```

### JavaScript Changes (notifications.js)
- Exposed `fetchUnreadCount()` globally
- Added focus event listener for badge updates

### JavaScript Changes (chat.html)
- Badge refresh on page load (1 second delay)
- Badge refresh every 10 seconds while on chat
- Badge refresh when leaving chat page

### 3. Badge Visibility on Open Chat Button
**Problem:** The unread message badge on "Open Chat" button was partially hidden/cut off.

**Solution:**
- Moved badge position from `top: -8px; right: -8px` to `top: -10px; right: -10px`
- Increased padding from `2px 6px` to `4px 8px` for better visibility
- Increased font size from `11px` to `12px`
- Added `overflow: visible` to parent button
- Added `z-index: 10` to ensure badge stays on top
- Added box shadow for better visual prominence

**Files Modified:**
- `main/templates/main/my_trips.html` - Fixed badge positioning on both "Open Chat" and "Manage Chat" buttons

## Testing
1. Open a chat with unread messages
2. Verify badge clears within 1-2 seconds
3. Test on mobile - send button should remain tappable
4. Navigate between chats - badge should update correctly
5. Check My Trips page - unread badges should be fully visible on Open Chat buttons
