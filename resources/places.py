import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user


places = Blueprint('places', 'places')

@places.route('/', methods=['GET'])
def places_index():
  result= models.Places.select()
  print('result of places select query')
  print(result)
  current_user_places_dicts = [model_to_dict(places) for places in current_user.places] 

  for places_dict in current_user_places_dicts:
      places_dict['user'].pop('password')
  return jsonify({
        'data': current_user_places_dicts,
        'message': f"Successfully found {len(current_user_places_dicts)} places",
        'status': 200
    }), 200

@places.route('/', methods=['POST'])
def create_places():
    payload = request.get_json() # this is like req.body in express
    print(payload)
    new_places = models.Places.create(
        name=payload['name'], 
        location=payload['location'],
        rating=payload['rating'],
        likes=payload['likes'],
        comments=payload['comments'],
        imageURL=payload['imageURL'],
        privateUse=payload['privateUse'],
        user=current_user.id
        )
    print(new_places)
    places_dict = model_to_dict(new_places)

    places_dict['user'].pop('password')

    return jsonify(
        data=places_dict,
        message='Successfully created place!',
        status=201
    ), 201

@places.route('/<id>', methods=['GET'])
def get_one_places(id):
    places = models.Places.get_by_id(id)
    print(places)
    return jsonify(
        data = model_to_dict(places),
        message = 'Success!!! 🎉',
        status = 200
    ), 200

@places.route('/<id>', methods=["PUT"])
def update_places(id):
    payload = request.get_json()
    query = models.Places.update(**payload).where(models.Places.id == id)
    query.execute()
    return jsonify(
        data = model_to_dict(models.Places.get_by_id(id)),
        status=200,
        message='resource updated successfully'
    ), 200

@places.route('/<id>', methods=['DELETE'])
def delete_places(id):
    query = models.Places.delete().where(models.Places.id == id)
    query.execute()
    return jsonify(
        data= model_to_dict(models.Places.get_by_id(id)),
        message='resource successfully deleted',
        status=200
    ), 200
