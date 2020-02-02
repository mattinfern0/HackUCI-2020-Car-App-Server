from flask import Blueprint, request, Response, jsonify
from app.models import car
from app.controller.carSelector import rateCars, user_choices_test, cars_test, database

car_controller = Blueprint('car_controller', __name__)
MAX_CARS_TO_SEND = 6


@car_controller.route('/', methods=['GET', 'POST'])
def getCars():
    if request.is_json:
        userData = request.get_json()
        print(userData)


    results = car.Car.query.all()
    serialized = [c.serialize() for c in results]
    rated_cars = rateCars(database, userData)

    sort_func = lambda e: e["points"]
    rated_cars.sort(key=sort_func, reverse=True)

    result_cars = []
    result_i = 0
    while (result_i < MAX_CARS_TO_SEND and  result_i < len(rated_cars)):
        result_cars.append(rated_cars[result_i])
        result_i += 1

    data = {"cars": result_cars}

    print(data)

    return jsonify(data)