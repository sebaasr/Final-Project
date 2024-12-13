import openai
import os
from flask import Flask, render_template, request
from models import TripPlanner, WeatherAPI, MapVisualizer
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

# Set the OpenAI API key
openai.api_key = "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"  # Replace with your actual key

class TripPlanner:
    def __init__(self, destination):
        self.destination = destination

    def get_suggestions(self):
        try:
            response = openai.Completion.create(
                model="gpt-3.5-turbo",  # Updated model
                prompt=f"Suggest a trip to {self.destination}",
                max_tokens=150
            )
            suggestions = response.choices[0].text.strip()
            return suggestions
        except Exception as e:
            return str(e)

# Set OpenAI API key securely from environment variables


# OpenWeatherMap API key (same concept, secure it using environment variables)
weather_api_key = os.getenv('09b6ce515dea1a42be18420b0f92ab43')  # Set your weather API key in the environment variables

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/plan_trip', methods=['POST'])
def plan_trip():
    destination = request.form['destination']

    # Get travel suggestions from GPT using the TripPlanner class
    trip_planner = TripPlanner(destination)
    suggestions = trip_planner.get_suggestions()

    # Get weather data using the WeatherAPI class
    weather_api = WeatherAPI(weather_api_key)
    weather = weather_api.get_weather(destination)

    # Debugging line to check the weather structure
    print(weather)  # Check the weather data in the console

    # Generate map and QR code for the trip using the MapVisualizer class
    map_visualizer = MapVisualizer(destination)
    map_visualizer.save_map(f"static/{destination}_map.html")
    map_visualizer.generate_qr_code(f"Destination: {destination}", f"static/{destination}_qr.png")

    # Return results to be rendered in the HTML template
    return render_template(
        'index.html',
        suggestions=suggestions,
        weather=weather,
        destination=destination
    )

if __name__ == '__main__':
    app.run(debug=True)
