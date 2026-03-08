from flask import Blueprint, request, jsonify
from models import Load
from schemas import load_schema, loads_schema
from marshmallow import ValidationError
from database import db

load_bp = Blueprint('load_bp', __name__)

@load_bp.route('/load', methods=['POST'])
def add_load():
    try:
        data = request.get_json()
        load_schema.load(data)
        
        new_load = Load(
            loading_point=data['loading_point'],
            unloading_point=data['unloading_point'],
            product_type=data['product_type'],
            truck_type=data['truck_type'],
            no_of_trucks=data['no_of_trucks'],
            weight=data['weight'],
            comment=data.get('comment', ''),
            shipper_id=data['shipper_id'],
            date=data['date']
        )
        db.session.add(new_load)
        db.session.commit()
        return jsonify({"message": "Load details added successfully", "load": load_schema.dump(new_load)}), 201
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

@load_bp.route('/load', methods=['GET'])
def get_loads():
    shipper_id = request.args.get('shipperId')
    loads = Load.query.filter_by(shipper_id=shipper_id).all()
    result = loads_schema.dump(loads)  # Serialize the loads
    return jsonify(result), 200  # Use jsonify to return a JSON response

@load_bp.route('/load/<load_id>', methods=['GET'])
def get_load(load_id):
    load = Load.query.get_or_404(load_id)
    result = load_schema.dump(load)  # Serialize the single load
    return jsonify(result), 200  # Use jsonify to return a JSON response

@load_bp.route('/load/<load_id>', methods=['PUT'])
def update_load(load_id):
    load = Load.query.get_or_404(load_id)
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    load.loading_point = data.get('loading_point', load.loading_point)
    load.unloading_point = data.get('unloading_point', load.unloading_point)
    load.product_type = data.get('product_type', load.product_type)
    load.truck_type = data.get('truck_type', load.truck_type)
    load.no_of_trucks = data.get('no_of_trucks', load.no_of_trucks)
    load.weight = data.get('weight', load.weight)
    load.comment = data.get('comment', load.comment)
    load.date = data.get('date', load.date)

    db.session.commit()
    result = load_schema.dump(load)
    return jsonify(result), 200

@load_bp.route('/load/<load_id>', methods=['DELETE'])
def delete_load(load_id):
    load = Load.query.get_or_404(load_id)
    db.session.delete(load)
    db.session.commit()
    return jsonify({"message": "Load deleted successfully"}), 204

