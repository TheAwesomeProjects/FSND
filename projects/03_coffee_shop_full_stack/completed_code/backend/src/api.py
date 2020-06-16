# import sys
# sys.path.insert(0, '..')

from flask import Flask, request, jsonify, abort
from flask_migrate import Migrate
from flask_cors import CORS

from .database.models import setup_db, db, Drink
from .auth.auth import requires_auth, AuthError
import json


app = Flask(__name__)
setup_db(app)
migrate = Migrate(app, db)
CORS(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET, POST, PATCH, DELETE')
    return response


# ROUTES


@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.order_by(Drink.id).all()
    drinks = [drink.short() for drink in drinks]

    if len(drinks) == 0:
        abort(404)

    return jsonify({
        "success": True,
        "drinks": drinks
    })


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drink_detail(payload):
    drinks = Drink.query.order_by(Drink.id).all()
    drinks = [drink.long() for drink in drinks]

    if len(drinks) == 0:
        abort(404)

    return jsonify({
        "success": True,
        "drinks": drinks
    })


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def create_drink(payload):
    body = request.get_json()

    new_title = body.get('title', None)
    new_recipe = json.dumps(body.get('recipe', None))

    try:
        drink = Drink(title=new_title, recipe=new_recipe)
        drink.insert()

        return jsonify({
            "success": True,
            "drinks": drink.long()
        })

    except Exception as e:
        abort(422)


@app.route('/drinks/<id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(payload, id):
    try:
        body = request.get_json()
        new_title = body.get('title', None)
        new_recipe = json.dumps(body.get('recipe', None))

        drink = Drink.query.filter(Drink.id == id).one_or_none()

        if drink is None:
            abort(404)

        drink.title = new_title
        drink.recipe = new_recipe
        drink.update()

        return jsonify({
            "success": True,
            "drinks": drink.long()
        })

    except Exception as e:
        if e.code == 404:
            abort(404)
        else:
            abort(422)


@app.route('/drinks/<id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(payload, id):
    try:
        drink = Drink.query.filter(Drink.id == id).one_or_none()

        if drink is None:
            abort(404)

        drink.delete()

        return jsonify({
            "success": True,
            "delete": id
        })

    except Exception as e:
        if e.code == 404:
            abort(404)
        else:
            abort(422)


# Error Handling


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(405)
def not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "method not allowed"
      }), 405


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
      "success": False,
      "error": 500,
      "message": "Internal Server Error"
      }), 500


@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
      "success": False,
      "error": error.status_code,
      "message": error.error['description']
      }), error.status_code


# if __name__ == '__main__':
#    app.run(debug=True, use_reloader=False)
