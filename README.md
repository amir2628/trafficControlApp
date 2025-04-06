# 🚦 Traffic Light Control System

A modern web-based traffic light control system built with Django that features:
- Real-time visual simulation of traffic light states
- Automated state transitions based on configurable durations
- Interactive dashboard for configuration updates
- AJAX-powered interface with no page reloads
- Responsive design with Bootstrap 5

![Screenshot](https://github.com/amir2628/trafficControlApp/blob/master/screenshots/app.png)

## ✨ Features
- **Visual Simulation**: Realistic traffic light display with active state highlighting
- **Dynamic Configuration**:
  - Adjust durations for Red, Yellow, and Green phases
  - Instant configuration updates without page refresh
- **Automated Cycling**:
  - Automatic state transitions based on configured durations
  - Countdown timer for current state
- **Dashboard**:
  - Real-time display of current configuration
  - Update history tracking
  - Responsive design for all screen sizes

## 🛠️ Installation
1. **Prerequisites**:
   - Python 3.9+
   - pip package manager

2. **Clone repository**:
   ```bash
   git clone https://github.com/amir2628/trafficControlApp.git
   cd trafficControlApp

3. **Set up virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

4. **Install dependencies**:
    ```bash
    pip install -r requirements.txt

5. **Database setup**:
    ```bash
    python manage.py migrate

6. **Run development server**:
    ```bash
    python manage.py runserver

## 🚀 Usage

1. Access the dashboard at http://localhost:8000
2. **Default Configuration**:

    - Red: 30s

    - Yellow: 5s

    - Green: 25s

    - Initial state: Red

3. **Update Configuration**:

    - Modify duration values in the form

    - Click "Update Settings"

    - Watch the simulation automatically adjust to new times

4. **Observe Automation**:

    - The system will automatically cycle through states

    - Countdown timer shows remaining time for current state

    - Current state highlighted in the visual display

## 📂 Project Structure
```
├── traffic_app/
│   ├── migrations/     # Database migrations
│   ├── static/         # CSS, JavaScript, and images
│   ├── templates/      # HTML templates
│   ├── admin.py        # Admin configuration
│   ├── apps.py         # App configuration
│   ├── forms.py        # Form definitions
│   ├── models.py       # Database models
│   ├── urls.py         # URL routing
│   └── views.py        # Business logic
├── traffic_control/    # Project settings
├── manage.py           # Django CLI tool
└── README.md           # This documentation
```

## ⚙️ Technical Stack
- **Backend**: Django 4.x

- **Frontend**:

    * Bootstrap 5

    * jQuery 3.6

    * Custom CSS/JavaScript

- **Database**: SQLite (default)