from flask import Blueprint, request, jsonify
from bson import ObjectId
from app import mongo
from app.utils import to_dict

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/', methods=['POST'])
def create_booking():
    data = request.json
    if not data or not data.get('user_id') or not data.get('destination_id'):
        return jsonify({"error": "Missing required fields"}), 400

    booking = {
        "user_id": data['user_id'],
        "destination_id": data['destination_id'],
        "status": "confirmed",
        "created_at": datetime.utcnow()
    }
    mongo.db.bookings.insert_one(booking)
    return jsonify({"message": "Booking created successfully"}), 201

@booking_bp.route('/<id>', methods=['GET'])
def get_booking(id):
    booking = mongo.db.bookings.find_one({"_id": ObjectId(id)})
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    return jsonify(to_dict(booking))
