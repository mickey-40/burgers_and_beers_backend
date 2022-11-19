import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user


allplaces = Blueprint('allplaces','allplaces')

@allplaces.route('/', methods=['GET'])
def places_index():
  result= models.Places.select()
  print('result of places select query')
  print(result)
  places_dicts = [model_to_dict(allplaces) for places in allplaces] 

  for places_dict in places_dicts:
      places_dict['user'].pop('password')
  return jsonify({
        'data': places_dicts,
        'message': f"Successfully found {len(places_dicts)} places",
        'status': 200
    }), 200