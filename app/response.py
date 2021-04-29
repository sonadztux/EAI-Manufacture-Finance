from flask import jsonify, make_response

def success(values, message):
    response = {
        'data' : values,
        'message': message
    }
    return make_response(jsonify(response)), 200

def badRequest(values, message):
    response = {
        'data' : values,
        'message': message
    }
    return make_response(jsonify(response)), 400