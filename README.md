# Trip Planner Application

This is a web that shows you the qr code and also the map of the destiny you wanna travel, also the weather.

## Features
- Get personalized trip suggestions from GPT-3.
- Fetch weather information for a given destination.
- View the destination map and QR code.

  Look at the repository and clone it

## Installation
 Install dependencies:
   ```
   pip install -r requirements.txt
   ```
 Create a folder called Static, there is gonna be the qr and the map

 should look like this
  smart_travel_planner/
├── app.py
├── models.py
├── templates/
│   └── index.html
├── static/
│   └── (Generated map and QR code files will be saved here)
└── requirements.txt
 Run the application:
   ```
   python app.py
   ```

## Usage
- Open your browser and go to `http://127.0.0.1:5000/`.
- Enter a destination in the input form to receive trip suggestions, weather information, and map/QR code.
