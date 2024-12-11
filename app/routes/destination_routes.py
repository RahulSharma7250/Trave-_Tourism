from flask import Blueprint, request, jsonify
from bson import ObjectId
from app import mongo
from app.utils import to_dict

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
