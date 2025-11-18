// Travel Tribe AI Chatbot - Enhanced Companion
(function() {
  'use strict';
  
  // User context tracking
  let userContext = {
    name: null,
    lastTopic: null,
    conversationHistory: [],
    preferences: {}
  };
  
  // Comprehensive Q&A Dataset
  const commonQA = {
    // General Travel Questions
    'how to book': 'To book a trip: 1) Browse trips on home page, 2) Click "Join Trip", 3) Start chatting with tribe members! No payment needed - it\'s free to join.',
    'is it free': 'Yes! Travel Tribe is completely FREE. You can join tribes, chat with members, and plan trips without any cost.',
    'how does it work': 'Simple! Create an account → Browse trips → Join a tribe → Chat with members → Plan together → Travel together! 🌍',
    'what is travel tribe': 'Travel Tribe is a platform to find travel buddies! Join tribes, meet like-minded travelers, and explore destinations together.',
    'safe to use': 'Yes! We prioritize safety. Always meet in public places, verify profiles, share itinerary with family, and trust your instincts.',
    'age limit': 'You must be 18+ to use Travel Tribe. We recommend traveling with age-appropriate groups.',
    'solo travel': 'Perfect for solo travelers! Join tribes to meet companions, share costs, and make friends while maintaining independence.',
    'group size': 'Trip groups vary from 2-20 members. Check each trip\'s member limit before joining.',
    'cancel trip': 'Yes! Go to "My Trips" → Find your trip → Click "Leave" button. You can leave anytime.',
    'create trip': 'Click "Create Trip" in navbar → Fill destination, dates, preferences → Post it! Others will join your tribe.',
    'chat feature': 'Real-time chat with tribe members! Share photos, plan itinerary, discuss details. Access via "Open Chat" button.',
    'payment': 'No payment on platform! Discuss and split costs directly with tribe members. We don\'t handle transactions.',
    'refund policy': 'Since we don\'t process payments, refunds are between tribe members. Discuss payment terms before booking.',
    'contact support': 'Email: support.travel_tribe@gmail.com | Instagram: @team_travel_tribe',
    
    // Destination Questions
    'best time to visit': 'Best times vary by destination. Use our Hunt feature to find best times for 40+ Indian destinations!',
    'visa requirements': 'Check official government websites for visa requirements. Requirements vary by destination and nationality.',
    'budget travel': 'Join tribes to split costs! Share accommodation, transport, and meals. Budget trips available for ₹5,000-15,000.',
    'luxury travel': 'We have luxury trips too! Dubai, international destinations, and premium experiences available.',
    'weekend trips': 'Yes! Many short weekend trips available. Filter by dates to find 2-3 day adventures.',
    'long trips': 'Absolutely! Find week-long or month-long adventures. Check trip duration before joining.',
    
    // Food & Accommodation
    'food options': 'Each trip specifies food preferences (Veg/Non-Veg/Both). Discuss dietary needs with tribe members.',
    'accommodation': 'Tribes decide together! Options include hotels, hostels, homestays, camping. Discuss in chat.',
    'vegetarian food': 'Many trips offer vegetarian options. Check trip details or ask tribe leader before joining.',
    
    // Safety & Security
    'verify members': 'Check member profiles, chat history, and reviews. Meet in public places first. Trust your instincts!',
    'emergency contact': 'Always share your itinerary with family. Keep emergency contacts handy. Stay connected with tribe.',
    'insurance': 'We recommend travel insurance for all trips. Arrange independently based on your needs.',
    
    // Technical Questions
    'app available': 'Currently web-based. Mobile app coming soon! Use browser on phone for now.',
    'notifications': 'Get chat notifications when tribe members message. Enable browser notifications for updates.',
    'edit profile': 'Go to Profile → Edit details → Save. Update your interests, bio, and preferences.',
    'delete account': 'Contact support at support.travel_tribe@gmail.com to delete your account.',
    'forgot password': 'Click "Forgot Password" on login page → Enter email → Verify OTP → Reset password.',
    
    // Platform Features
    'hunt feature': 'Discover must-visit places and must-try foods! Search 40+ Indian destinations with detailed info.',
    'my trips': 'View all your trips in "My Trips" page. See joined tribes and created trips in one place.',
    'leave tribe': 'Go to "My Trips" → Find trip → Click "Leave" → Confirm. You can leave anytime!',
    'tribe leader': 'Trip creator is the tribe leader. They manage the trip and coordinate with members.',
    'member limit': 'Each trip has a member limit (shown as X/Y members). Join before it fills up!',
  };

  // Chatbot knowledge base
  const knowledgeBase = {
    trips: [
      { 
        name: "Manali", 
        category: "Within Country", 
        type: "Adventure, Mountains",
        description: "A beautiful hill station perfect for adventure seekers and nature lovers",
        bestTime: "October to June",
        activities: "Skiing, paragliding, trekking, river rafting"
      },
      { 
        name: "Vizag", 
        category: "Within Country", 
        type: "Beach, Relaxation",
        description: "Coastal city with pristine beaches and scenic beauty",
        bestTime: "October to March",
        activities: "Beach activities, water sports, sightseeing"
      },
      { 
        name: "Varanasi", 
        category: "Within Country", 
        type: "Culture, Spiritual",
        description: "Ancient spiritual city on the banks of Ganges",
        bestTime: "November to February",
        activities: "Temple visits, Ganga Aarti, boat rides, cultural exploration"
      },
      { 
        name: "Goa", 
        category: "Within Country", 
        type: "Beach, Party",
        description: "India's beach paradise with vibrant nightlife",
        bestTime: "November to February",
        activities: "Beach parties, water sports, nightlife, Portuguese heritage"
      },
      { 
        name: "Ladakh", 
        category: "Within Country", 
        type: "Adventure, Mountains",
        description: "High-altitude desert with stunning landscapes",
        bestTime: "May to September",
        activities: "Bike trips, trekking, monastery visits, camping"
      },
      { 
        name: "Dubai", 
        category: "Outside Country", 
        type: "Luxury, Shopping",
        description: "Modern metropolis with luxury shopping and architecture",
        bestTime: "November to March",
        activities: "Shopping, desert safari, skyscraper visits, luxury dining"
      }
    ],
    
    responses: {
      greeting: [
        "Hello friend! 👋 I'm so excited to help you plan your next adventure! What's on your mind?",
        "Hi there! 🌍 I'm your travel companion. Tell me, what kind of experience are you looking for?",
        "Hey! 😊 Great to see you! I'm here to help with anything travel-related. What would you like to know?",
        "Welcome back! 🎒 Ready to explore the world together? Ask me anything!"
      ],
      
      personal: [
        "I'm your AI travel companion! 🤖 I'm here 24/7 to help you discover amazing destinations, plan trips, and connect with fellow travelers. Think of me as your friendly travel buddy who knows everything about Travel Tribe!",
        "I'm an AI assistant created to make your travel planning easier and more fun! 😊 I can help you find trips, answer questions, give recommendations, and even chat about your travel dreams!",
        "Great question! I'm your personal travel guide on this platform. I know all about the trips, destinations, and features here. But more than that, I'm here to listen and help you plan the perfect adventure!"
      ],
      
      feelings: [
        "I'm doing great, thanks for asking! 😊 I'm always excited when I get to help someone plan their next adventure. How are YOU feeling today?",
        "I'm wonderful! 🌟 Helping travelers like you makes me happy. How about you? Feeling adventurous today?",
        "I'm fantastic! 💫 Every conversation is a new adventure for me. What's your mood like? Ready to explore?"
      ],
      
      thanks: [
        "You're very welcome! 😊 I'm always here if you need anything else. Happy travels!",
        "My pleasure! 🌟 That's what I'm here for. Feel free to ask me anything anytime!",
        "Anytime, friend! 🎒 I love helping out. Safe travels and have an amazing adventure!"
      ],
      
      compliment: [
        "Aww, thank you! 🥰 You're pretty awesome yourself! Now, how can I help make your travel dreams come true?",
        "That's so kind of you! 😊 You're making my day! What can I do for you today?",
        "Thank you so much! 💙 You're wonderful too! Let's plan something amazing together!"
      ],
      
      trips: [
        "We have amazing trips available! 🗺️\n\n" +
        "Within India:\n" +
        "• Manali - Mountain adventure\n" +
        "• Goa - Beach paradise\n" +
        "• Varanasi - Cultural experience\n" +
        "• Ladakh - Ultimate adventure\n\n" +
        "International:\n" +
        "• Dubai - Luxury getaway\n\n" +
        "Which destination interests you?"
      ],
      
      join: [
        "Joining a tribe is easy! 🎉\n\n" +
        "1. Browse trips on the home page\n" +
        "2. Click 'View Details' on any trip\n" +
        "3. Click 'Join Trip' button\n" +
        "4. Start chatting with tribe members!\n\n" +
        "You can join multiple tribes and leave anytime."
      ],
      
      create: [
        "Want to create your own trip? 🚀\n\n" +
        "1. Click 'Create Trip' on home page\n" +
        "2. Fill in destination, dates, and preferences\n" +
        "3. Set member limit and interests\n" +
        "4. Post it and wait for tribe members!\n\n" +
        "You'll be the tribe leader!"
      ],
      
      popular: [
        "Our most popular destinations right now: ⭐\n\n" +
        "🏔️ Manali - Perfect for adventure seekers\n" +
        "🏖️ Goa - Beach lovers paradise\n" +
        "🏔️ Ladakh - Ultimate mountain experience\n" +
        "🕌 Varanasi - Rich cultural heritage\n" +
        "🌆 Dubai - Luxury and modern architecture\n\n" +
        "Which one catches your eye?"
      ],
      
      chat: [
        "Our chat feature is awesome! 💬\n\n" +
        "• Real-time messaging with tribe members\n" +
        "• Share photos and videos\n" +
        "• Plan your itinerary together\n" +
        "• Safety warnings included\n\n" +
        "Join a trip to access the chat!"
      ],
      
      safety: [
        "Your safety is our priority! 🛡️\n\n" +
        "• Verify member profiles before meeting\n" +
        "• Meet in public places first\n" +
        "• Share your itinerary with family\n" +
        "• Trust your instincts\n" +
        "• Use our in-app chat for communication\n\n" +
        "Travel smart, travel safe!"
      ],
      
      budget: [
        "Great question about budget! 💰\n\n" +
        "Travel costs vary by destination:\n" +
        "• Manali/Goa: ₹5,000-15,000 per person\n" +
        "• Ladakh: ₹15,000-30,000 per person\n" +
        "• Dubai: ₹40,000-80,000 per person\n\n" +
        "When you join a tribe, you can discuss and split costs with members. Many tribes share accommodation and transport to save money!"
      ],
      
      solo: [
        "Solo travel is amazing! 🎒\n\n" +
        "Our platform is perfect for solo travelers:\n" +
        "• Join tribes to meet like-minded people\n" +
        "• Travel together but maintain independence\n" +
        "• Share costs and experiences\n" +
        "• Make lifelong friends\n\n" +
        "Many of our members started as solo travelers and found their travel tribe here!"
      ],
      
      weather: [
        "Weather planning is important! ☀️\n\n" +
        "Best times to visit:\n" +
        "• Manali: Oct-June (avoid monsoon)\n" +
        "• Goa: Nov-Feb (pleasant weather)\n" +
        "• Ladakh: May-Sep (roads open)\n" +
        "• Varanasi: Nov-Feb (cool weather)\n" +
        "• Dubai: Nov-Mar (not too hot)\n\n" +
        "Which destination interests you?"
      ],
      
      food: [
        "Food is a big part of travel! 🍽️\n\n" +
        "Each trip has food preferences:\n" +
        "• Veg, Non-Veg, or Both options\n" +
        "• Local cuisine experiences\n" +
        "• Group meals to bond with tribe\n" +
        "• Must-try foods listed for each destination\n\n" +
        "You can discuss food preferences with your tribe members in the chat!"
      ],
      
      confused: [
        "No worries, I'm here to help! 😊\n\n" +
        "Let me break it down simply:\n" +
        "1. Browse trips on home page\n" +
        "2. Click 'Join Trip' on ones you like\n" +
        "3. Chat with tribe members\n" +
        "4. Plan together and travel!\n\n" +
        "What specific part would you like me to explain more?"
      ],
      
      encouragement: [
        "You've got this! 🌟 Taking the first step is always the hardest, but I promise it's worth it. Thousands of travelers have found amazing experiences through our platform. Your adventure is waiting!",
        "I believe in you! 💪 Travel is about stepping out of your comfort zone, and you're already doing that by being here. Start small, join a tribe, and see where it takes you!",
        "Don't worry, everyone feels this way at first! 🤗 But remember, every expert traveler was once a beginner. Take your time, ask questions, and when you're ready, your tribe will be waiting!"
      ],
      
      default: [
        "Hmm, I'm not quite sure about that specific thing, but I'm here to help! 🤔\n\n" +
        "I can chat about:\n" +
        "🗺️ Destinations and trips\n" +
        "👥 Finding travel buddies\n" +
        "💰 Budget and costs\n" +
        "🍽️ Food and preferences\n" +
        "☀️ Weather and best times\n" +
        "🛡️ Safety tips\n" +
        "💬 How the platform works\n\n" +
        "Or just chat with me about travel! What's on your mind?"
      ]
    }
  };
  
  // Initialize chatbot
  function initChatbot() {
    const container = document.getElementById('chatbot-container');
    const toggle = document.getElementById('chatbot-toggle');
    const window = document.getElementById('chatbot-window');
    const close = document.getElementById('chatbot-close');
    const input = document.getElementById('chatbot-input');
    const send = document.getElementById('chatbot-send');
    const messages = document.getElementById('chatbot-messages');
    const quickActions = document.querySelectorAll('.quick-action-btn');
    const perryImg = container ? container.getAttribute('data-perry-img') : '';
    
    // Toggle chatbot
    toggle.addEventListener('click', () => {
      window.classList.toggle('active');
      if (window.classList.contains('active')) {
        input.focus();
      }
    });
    
    // Close chatbot
    close.addEventListener('click', () => {
      window.classList.remove('active');
    });
    
    // Send message
    send.addEventListener('click', sendMessage);
    input.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        sendMessage();
      }
    });
    
    // Quick actions
    quickActions.forEach(btn => {
      btn.addEventListener('click', () => {
        const question = btn.getAttribute('data-question');
        input.value = question;
        sendMessage();
      });
    });
    
    function sendMessage() {
      const message = input.value.trim();
      if (!message) return;
      
      // Add user message
      addMessage(message, 'user');
      input.value = '';
      
      // Show typing indicator
      showTyping();
      
      // Get bot response
      setTimeout(() => {
        hideTyping();
        const response = getBotResponse(message);
        addMessage(response, 'bot');
      }, 1000 + Math.random() * 1000);
    }
    
    function addMessage(text, type) {
      const messageDiv = document.createElement('div');
      messageDiv.className = `chatbot-message ${type}-message`;
      
      const avatar = document.createElement('div');
      avatar.className = 'message-avatar';
      if (type === 'bot') {
        avatar.innerHTML = `<img src="${perryImg}" alt="AI Assistant" class="message-avatar-img">`;
      } else {
        avatar.innerHTML = '<i class="fas fa-user"></i>';
      }
      
      const content = document.createElement('div');
      content.className = 'message-content';
      
      // Convert newlines to <br> and preserve formatting
      const formattedText = text.replace(/\n/g, '<br>');
      content.innerHTML = `<p>${formattedText}</p>`;
      
      messageDiv.appendChild(avatar);
      messageDiv.appendChild(content);
      messages.appendChild(messageDiv);
      
      // Scroll to bottom
      messages.scrollTop = messages.scrollHeight;
    }
    
    function showTyping() {
      const typingDiv = document.createElement('div');
      typingDiv.className = 'chatbot-message bot-message';
      typingDiv.id = 'typing-indicator';
      
      const avatar = document.createElement('div');
      avatar.className = 'message-avatar';
      avatar.innerHTML = `<img src="${perryImg}" alt="AI Assistant" class="message-avatar-img">`;
      
      const content = document.createElement('div');
      content.className = 'message-content typing-indicator';
      content.innerHTML = '<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';
      
      typingDiv.appendChild(avatar);
      typingDiv.appendChild(content);
      messages.appendChild(typingDiv);
      messages.scrollTop = messages.scrollHeight;
    }
    
    function hideTyping() {
      const typing = document.getElementById('typing-indicator');
      if (typing) {
        typing.remove();
      }
    }
    
    function getBotResponse(message) {
      const lowerMessage = message.toLowerCase();
      
      // Store in conversation history
      userContext.conversationHistory.push({ role: 'user', message: message });
      
      // Check common Q&A first
      for (const [keyword, answer] of Object.entries(commonQA)) {
        if (lowerMessage.includes(keyword)) {
          return answer;
        }
      }
      
      // Check if asking about specific destination from Hunt database
      if (typeof huntDatabase !== 'undefined') {
        for (const [key, data] of Object.entries(huntDatabase)) {
          if (lowerMessage.includes(key) || lowerMessage.includes(data.name.toLowerCase())) {
            return `🌍 ${data.name}, ${data.state}\n\n` +
                   `📍 Must Visit: ${data.places.slice(0, 3).map(p => p.name).join(', ')}\n` +
                   `🍽️ Must Try: ${data.foods.slice(0, 3).map(f => f.name).join(', ')}\n\n` +
                   `Want more details? Use the Hunt section to explore all places and foods in ${data.name}!`;
          }
        }
      }
      
      // Personal questions about the bot
      if (lowerMessage.match(/\b(who are you|what are you|your name|about you)\b/)) {
        userContext.lastTopic = 'personal';
        return getRandomResponse('personal');
      }
      
      // How are you / feelings
      if (lowerMessage.match(/\b(how are you|how're you|how r u|you okay|you good)\b/)) {
        return getRandomResponse('feelings');
      }
      
      // Thanks
      if (lowerMessage.match(/\b(thank|thanks|thx|appreciate|grateful)\b/)) {
        return getRandomResponse('thanks');
      }
      
      // Compliments
      if (lowerMessage.match(/\b(awesome|great|amazing|wonderful|helpful|nice|good bot|love you)\b/)) {
        return getRandomResponse('compliment');
      }
      
      // Greeting
      if (lowerMessage.match(/\b(hi|hello|hey|greetings|sup|yo)\b/)) {
        return getRandomResponse('greeting');
      }
      
      // Budget questions
      if (lowerMessage.match(/\b(budget|cost|price|expensive|cheap|afford|money)\b/)) {
        userContext.lastTopic = 'budget';
        return getRandomResponse('budget');
      }
      
      // Solo travel
      if (lowerMessage.match(/\b(solo|alone|by myself|single traveler)\b/)) {
        userContext.lastTopic = 'solo';
        return getRandomResponse('solo');
      }
      
      // Weather
      if (lowerMessage.match(/\b(weather|climate|season|temperature|rain|hot|cold)\b/)) {
        userContext.lastTopic = 'weather';
        return getRandomResponse('weather');
      }
      
      // Food
      if (lowerMessage.match(/\b(food|eat|cuisine|restaurant|veg|non-veg|meal)\b/)) {
        userContext.lastTopic = 'food';
        return getRandomResponse('food');
      }
      
      // Confusion / help
      if (lowerMessage.match(/\b(confused|don't understand|help|lost|what|how does)\b/)) {
        return getRandomResponse('confused');
      }
      
      // Encouragement needed
      if (lowerMessage.match(/\b(scared|nervous|worried|afraid|anxious|first time)\b/)) {
        return getRandomResponse('encouragement');
      }
      
      // Trips/Destinations
      if (lowerMessage.match(/\b(trip|destination|place|where|available|show me|list)\b/)) {
        userContext.lastTopic = 'trips';
        return getRandomResponse('trips');
      }
      
      // Join tribe
      if (lowerMessage.match(/\b(join|how to join|joining|become member)\b/)) {
        userContext.lastTopic = 'join';
        return getRandomResponse('join');
      }
      
      // Create trip
      if (lowerMessage.match(/\b(create|post|start|make|add|new trip)\b/)) {
        userContext.lastTopic = 'create';
        return getRandomResponse('create');
      }
      
      // Popular destinations
      if (lowerMessage.match(/\b(popular|best|top|recommend|suggest|famous)\b/)) {
        userContext.lastTopic = 'popular';
        return getRandomResponse('popular');
      }
      
      // Chat feature
      if (lowerMessage.match(/\b(chat|message|talk|communicate|conversation)\b/)) {
        userContext.lastTopic = 'chat';
        return getRandomResponse('chat');
      }
      
      // Safety
      if (lowerMessage.match(/\b(safe|safety|secure|trust|danger|risk)\b/)) {
        userContext.lastTopic = 'safety';
        return getRandomResponse('safety');
      }
      
      // Specific destinations with detailed info
      const destinations = ['manali', 'goa', 'ladakh', 'varanasi', 'vizag', 'dubai'];
      for (const dest of destinations) {
        if (lowerMessage.includes(dest)) {
          const trip = knowledgeBase.trips.find(t => t.name.toLowerCase() === dest);
          if (trip) {
            userContext.lastTopic = dest;
            return `${trip.name} - ${trip.description} 🌟\n\n` +
                   `📍 Type: ${trip.type}\n` +
                   `🗓️ Best Time: ${trip.bestTime}\n` +
                   `🎯 Activities: ${trip.activities}\n` +
                   `📂 Category: ${trip.category}\n\n` +
                   `Want to visit ${trip.name}? Check the home page for available trips, or create your own tribe!`;
          }
        }
      }
      
      // Context-aware follow-up
      if (userContext.lastTopic && lowerMessage.match(/\b(yes|yeah|yep|sure|okay|tell me more|more info)\b/)) {
        if (userContext.lastTopic === 'trips') {
          return getRandomResponse('popular');
        } else if (userContext.lastTopic === 'join') {
          return "Great! 🎉 Just head to the home page, browse the trips, and click 'Join Trip' on any that interest you. You'll instantly be part of that tribe and can start chatting with members!";
        }
      }
      
      // Default response with personality
      return getRandomResponse('default');
    }
    
    function getRandomResponse(type) {
      const responses = knowledgeBase.responses[type];
      return responses[Math.floor(Math.random() * responses.length)];
    }
  }
  
  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initChatbot);
  } else {
    initChatbot();
  }
})();
