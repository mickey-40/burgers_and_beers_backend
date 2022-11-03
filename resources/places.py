import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict


places = Blueprint('places', 'places')

@places.route('/', methods=['GET'])
def places_index():
  result= models.Places.select()
  print('result of places select query')
  print(result)