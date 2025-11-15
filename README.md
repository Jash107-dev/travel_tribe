# 🌍 Travel Tribe - Connect, Explore, Adventure

A Django-based travel companion platform where travelers can find travel buddies, join tribes, discover destinations, and plan adventures together.

![Travel Tribe](https://img.shields.io/badge/Django-4.2-green)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

### 🎯 Core Features
- **User Authentication** - Secure login, registration, and profile management
- **Travel Tribes** - Create and join travel groups
- **Trip Planning** - Plan trips with dates, destinations, and preferences
- **Real-time Chat** - Chat with tribe members
- **Destination Discovery** - Browse trips by category (Within Country/International)
- **Hunt Feature** - Discover must-visit places and must-try foods across India (40+ destinations)
- **AI Chatbot** - Perry the Platypus assistant to help with travel queries

### 🎨 Design Features
- Modern, responsive UI with vibrant colors
- Gradient cards with hover effects
- Professional blue color scheme
- Mobile-friendly design
- Smooth animations and transitions

### 🔍 Hunt Section
Comprehensive database of Indian destinations with:
- Must-visit places (8 per destination)
- Must-try foods (8 per destination)
- 40+ destinations across all Indian states
- Search functionality with popular tags

## 🚀 Tech Stack

- **Backend:** Django 4.2+
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (Development) / MySQL (Production)
- **Icons:** Font Awesome 6.4
- **Fonts:** Poppins, Inter

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Git

### Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/travel_tribe.git
cd travel_tribe
```

2. **Create virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create superuser**
```bash
python manage.py createsuperuser
```

6. **Collect static files**
```bash
python manage.py collectstatic
```

7. **Run development server**
```bash
python manage.py runserver
```

8. **Open browser**
```
http://127.0.0.1:8000
```

## 🌐 Deployment

### PythonAnywhere (Recommended - FREE)
See `PYTHONANYWHERE_DEPLOYMENT.md` for detailed instructions.

### Other Options
- **Render** - See `DEPLOYMENT_GUIDE.md`
- **Railway** - See `DEPLOYMENT_GUIDE.md`
- **Heroku** - Traditional deployment

## 📁 Project Structure

```
travel_tribe/
├── main/                      # Main Django app
│   ├── static/               # Static files
│   │   ├── css/             # Stylesheets
│   │   ├── js/              # JavaScript files
│   │   └── img/             # Images
│   ├── templates/           # HTML templates
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   └── urls.py              # URL routing
├── travel_tribe/            # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL config
│   └── wsgi.py              # WSGI config
├── media/                   # User uploads
├── staticfiles/            # Collected static files
├── manage.py               # Django management
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🎨 Color Scheme

- **Primary:** #2563eb (Blue)
- **Success:** #10b981 (Green)
- **Warning:** #f59e0b (Orange)
- **Accent:** #ec4899 (Pink)
- **Purple:** #7c3aed (Purple)

## 📸 Screenshots

### Home Page
- Hero section with beach background
- Active Travel Tribes with colorful cards
- Popular Destinations
- Hunt section for discovering places

### Hunt Feature
- Search for destinations
- Must-visit places
- Must-try foods
- 40+ Indian destinations

### Chat Feature
- Real-time messaging
- Tribe member communication
- Media sharing

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License.

## 👥 Contact

- **Email:** support.travel_tribe@gmail.com
- **Instagram:** [@team_travel_tribe](https://instagram.com/team_travel_tribe)

## 🙏 Acknowledgments

- Font Awesome for icons
- Google Fonts for typography
- Unsplash for images
- Django community

## 📊 Features Roadmap

- [ ] Social media integration
- [ ] Trip reviews and ratings
- [ ] Payment integration
- [ ] Mobile app
- [ ] Advanced search filters
- [ ] Trip recommendations AI
- [ ] Multi-language support

---

Made with ❤️ by Travel Tribe Team

**Start your adventure today!** 🌍✈️
