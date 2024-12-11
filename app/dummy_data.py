from app import mongo
from datetime import datetime

# Dummy data to insert
dummy_data = [
    {
        "destination_id": "uuid1",
        "name": "Paris",
        "region": "Europe",
        "type": "Historical",
        "description": "A beautiful city with rich culture and landmarks.",
        "images": ["url1", "url2"],
        "highlights": ["Eiffel Tower", "Louvre Museum"],
        "best_time_to_visit": "April to October"
    },
    {
        "destination_id": "uuid2",
        "name": "Tokyo",
        "region": "Asia",
        "type": "Modern",
        "description": "A bustling metropolis known for technology, shopping, and entertainment.",
        "images": ["url3", "url4"],
        "highlights": ["Shibuya Crossing", "Tokyo Tower"],
        "best_time_to_visit": "March to May"
    },
    {
        "destination_id": "uuid3",
        "name": "New York City",
        "region": "North America",
        "type": "Urban",
        "description": "The city that never sleeps, known for its skyscrapers and iconic landmarks.",
        "images": ["url5", "url6"],
        "highlights": ["Statue of Liberty", "Central Park"],
        "best_time_to_visit": "April to June"
    },
    {
        "destination_id": "uuid4",
        "name": "Sydney",
        "region": "Australia",
        "type": "Coastal",
        "description": "A beautiful city with stunning beaches and landmarks.",
        "images": ["url7", "url8"],
        "highlights": ["Sydney Opera House", "Bondi Beach"],
        "best_time_to_visit": "November to March"
    },
    {
        "destination_id": "uuid5",
        "name": "Rome",
        "region": "Europe",
        "type": "Historical",
        "description": "A city steeped in history, with ancient ruins and museums.",
        "images": ["url9", "url10"],
        "highlights": ["Colosseum", "Vatican City"],
        "best_time_to_visit": "May to October"
    },
    {
        "destination_id": "uuid6",
        "name": "Cape Town",
        "region": "Africa",
        "type": "Coastal",
        "description": "A city known for its stunning landscapes and natural beauty.",
        "images": ["url11", "url12"],
        "highlights": ["Table Mountain", "Robben Island"],
        "best_time_to_visit": "November to March"
    },
    {
        "destination_id": "uuid7",
        "name": "Rio de Janeiro",
        "region": "South America",
        "type": "Beach",
        "description": "A vibrant city known for its carnival, beaches, and lively culture.",
        "images": ["url13", "url14"],
        "highlights": ["Christ the Redeemer", "Copacabana Beach"],
        "best_time_to_visit": "December to March"
    },
    {
        "destination_id": "uuid8",
        "name": "Dubai",
        "region": "Middle East",
        "type": "Modern",
        "description": "A futuristic city known for its skyscrapers and luxury shopping.",
        "images": ["url15", "url16"],
        "highlights": ["Burj Khalifa", "Palm Jumeirah"],
        "best_time_to_visit": "November to March"
    },
    {
        "destination_id": "uuid9",
        "name": "Machu Picchu",
        "region": "South America",
        "type": "Historical",
        "description": "An ancient Incan city located in the Andes Mountains.",
        "images": ["url17", "url18"],
        "highlights": ["Inca Trail", "Sun Gate"],
        "best_time_to_visit": "April to October"
    },
    {
        "destination_id": "uuid10",
        "name": "London",
        "region": "Europe",
        "type": "Urban",
        "description": "A city known for its history, culture, and iconic landmarks.",
        "images": ["url19", "url20"],
        "highlights": ["Big Ben", "London Eye"],
        "best_time_to_visit": "May to September"
    }
]

# Insert data into the 'destinations' collection
mongo.db.destinations.insert_many(dummy_data)
print("Dummy data inserted successfully.")
