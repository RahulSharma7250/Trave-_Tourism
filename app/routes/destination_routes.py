from flask import Blueprint, request, jsonify
from bson import ObjectId
from app import mongo
from app.utils import to_dict
from app.dummy_data import dummy_data 

destination_bp = Blueprint('destination', __name__)

@destination_bp.route('/', methods=['GET'])
def get_all_destinations():
    destinations = mongo.db.destinations.find()
    return jsonify([to_dict(dest) for dest in destinations])

@destination_bp.route('/<id>', methods=['GET'])
def get_destination(id):
    destination = mongo.db.destinations.find_one({"_id": ObjectId(id)})
    if not destination:
        return jsonify({"error": "Destination not found"}), 404
    return jsonify(to_dict(destination))

@destination_bp.route('/add-dummy', methods=['POST'])
def add_dummy_data():
    # Insert the dummy data from the external file into MongoDB
    mongo.db.destinations.insert_many(dummy_data)
    
    return jsonify({"message": "Dummy data added successfully!"}), 201
