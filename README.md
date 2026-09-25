# Manipur AI Trip Planner

A Python-based AI Trip Planner for generating personalized travel itineraries for destinations in Manipur.

The system recommends destinations based on user preferences, budget, interests, and distance. It then optimizes the travel route and generates a day-wise itinerary.

## Features

- Destination recommendation
- User preference handling
- Budget planning
- Route optimization
- Day-wise itinerary generation
- SQLite destination database
- FastAPI REST API
- Flutter frontend integration

## Recommendation Method

The system uses a weighted multi-criteria scoring approach.

The recommendation score is calculated using:

Final Score =
0.60 × Preference Score
+ 0.25 × Budget Score
+ 0.15 × Distance Score

The preference score is based on the user's selected interests.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- SQLite
- Pandas
- Flutter
- Dart
- REST API
- JSON

Dataset

The project uses a dataset containing information about Manipur tourist destinations.

The dataset contains information such as:

Destination name
District
Category
Description
Latitude and longitude
Distance from Imphal
Estimated visit duration
Entry fee
Estimated transportation cost
Interest-based scores
Best season
How to Run
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/manipur-ai-trip-planner.git
2. Open the project
cd Ai-trip-planner
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment

Windows PowerShell:

.venv\Scripts\Activate.ps1
5. Install dependencies
pip install -r requirements.txt
6. Create the database
python database/database.py
7. Start the FastAPI server
python -m uvicorn api:app --host 0.0.0.0 --port 8000 --reload

The API will be available at:

http://127.0.0.1:8000

Swagger API documentation:

http://127.0.0.1:8000/docs
API Endpoint
POST /plan-trip

Example request:

{
  "budget": 10000,
  "days": 3,
  "travelers": 2,
  "interests": ["nature"]
}

The API returns the generated itinerary and budget information.

Flutter Integration

The Flutter application communicates with the FastAPI backend through HTTP requests.

Example:

Flutter
   ↓
POST /plan-trip
   ↓
FastAPI
   ↓
TripPlanner
   ↓
Recommendation + Route + Itinerary
   ↓
JSON response
   ↓
Flutter
Current Limitations
Starting location is currently handled as Imphal by the backend.
The itinerary currently uses a simple destination-per-day distribution.
The recommendation system uses a scoring-based approach rather than a trained machine-learning model.
Travel time and real-time traffic are not currently considered.
Destination information depends on the available dataset.
Future Improvements
Dynamic itinerary generation based on visit duration
User-defined starting location
Real-time route information
More tourism destinations
Improved budget estimation
More sophisticated recommendation algorithms
Meiteilon language and speech integration
License
This project is developed for academic/project purposes.