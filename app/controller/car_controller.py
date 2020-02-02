from flask import Blueprint, request, Response, jsonify
from app.models import car
from app.controller.carSelector import rateCars, user_choices_test, cars_test

car_controller = Blueprint('car_controller', __name__)

@car_controller.route('/')
def getCars():
    if request.is_json:
        userData = request.get_json()
        print(userData)


    results = car.Car.query.all()
    serialized = [c.serialize() for c in results]
    rated_cars = rateCars(cars_test, user_choices_test)

    sort_func = lambda e: e["points"]
    rated_cars.sort(key=sort_func, reverse=True)

    result_cars = []
    print(len(rated_cars))
    result_i = 0
    while (result_i < 5 and  result_i < len(rated_cars)):
        result_cars.append(rated_cars[result_i])
        result_i += 1

    data = {"cars": result_cars}
    
    

    print(data)

    return jsonify(data)