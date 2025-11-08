# 🌦️ Weather App – Hackathon Practice Project

Hey! This is my simple Weather App I built for Hackathon practice.  
It lets you quickly check the weather of any city in a fun and easy way.  

This repo contains **two versions**:  
1. Flask version  
2. Django version  

---

## About the Project

- A small project to fetch real-time weather updates 🌤️  
- Enter any city and instantly see the current weather  
- Clean and beginner-friendly design with input boxes and background images  
- Perfect for Hackathon practice or learning Flask/Django  

---

## Features

- Type a city name → see the weather instantly ☀️⛅🌧️  
- Simple, responsive design  
- Works locally and can be deployed later  

---

## 🔹 Flask Version – Getting Started

Follow these steps to run it on your PC:

1️⃣ **Download the project from GitHub**  

*git clone https://github.com/aryansingh1013/Weather-App.git*  
*cd Weather-App/flask_version*

2️⃣ **Create a virtual environment**  

*python -m venv env*  
*# This creates a folder `env` for project dependencies.*

3️⃣ **Activate the environment**  

*For Windows PowerShell:*  
*.\env\Scripts\activate*  

*For Linux / MacOS:*  
*source env/bin/activate*

4️⃣ **Install dependencies**  

*pip install -r requirements.txt*  
*# This installs Flask, Requests, and other required packages.*

5️⃣ **Run the app**  

*python app.py*  
*# Open your browser and go to http://127.0.0.1:5000/*  

Enter any city to see the weather 🌤️  

---

## 🔹 Django Version – Getting Started

1️⃣ **Navigate to Django folder**  

*cd Weather-App/django_version*

2️⃣ **Create a virtual environment**  

*python -m venv env*  
*.\env\Scripts\activate*  *(Windows)*  
*source env/bin/activate*  *(Linux / MacOS)*

3️⃣ **Install dependencies**  

*pip install -r ../flask_version/requirements.txt*  
*(or create a Django-specific requirements file if needed)*

4️⃣ **Apply migrations**  

*python manage.py migrate*

5️⃣ **Run the Django server**  

*python manage.py runserver*  
*# Open your browser and go to http://127.0.0.1:8000/*  

Enter any city to see the weather 🌤️  

---

## ⚡ Notes

- Make sure Python 3.10+ is installed  
- Always activate the virtual environment before installing packages or running the app  
- Flask runs on port **5000**, Django runs on port **8000** by default  
- You can deploy both versions later using standard deployment practices  

---

Have fun exploring the app! 🌦️
