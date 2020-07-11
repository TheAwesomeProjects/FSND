# import sys
# sys.path.insert(0, '..')

from flask import Flask, request, jsonify, abort
from flask_migrate import Migrate
from flask_cors import CORS

from .database.models import setup_db, db, Tea, Catalog, Order, Client, Admin, Company
from .auth.auth import requires_auth, AuthError


def create_app(env='PROD'):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app, env)
    migrate = Migrate(app, db)
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE')
        return response

    # ROUTES

    @app.route('/tea', methods=['GET'])
    def get_tea():
        tea_list = Tea.query.order_by(Tea.id).all()

        if len(tea_list) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'tea_list': [tea.format() for tea in tea_list],
            'total_positions': len(tea_list)
        })

    @app.route('/tea', methods=['POST'])
    @requires_auth('post:tea')
    def create_tea(payload):
        body = request.get_json()

        new_title = body.get('title', None)
        new_tea_type = body.get('tea_type', None)
        new_code = body.get('code', None)
        new_packaging = body.get('packaging', None)
        new_price = body.get('price', None)
        new_description = body.get('description', None)
        new_ingredients = body.get('ingredients', None)
        new_instruction = body.get('instruction', None)
        new_tea_quantity = body.get('tea_quantity', None)

        try:
            tea = Tea(title=new_title, tea_type=new_tea_type, code=new_code, packaging=new_packaging, price=new_price,
                      description=new_description, ingredients=new_ingredients, instruction=new_instruction,
                      tea_quantity=new_tea_quantity)
            tea.insert()

            return jsonify({
                'success': True,
                'created': tea.id,
                'total_positions': len(Tea.query.all())
            })

        except Exception as e:
            abort(422, e)

    @app.route('/tea/<id>', methods=['PATCH'])
    @requires_auth('patch:tea')
    def update_tea(payload, id):
        try:
            body = request.get_json()

            new_title = body.get('title', None)
            new_tea_type = body.get('tea_type', None)
            new_code = body.get('code', None)
            new_packaging = body.get('packaging', None)
            new_price = body.get('price', None)
            new_description = body.get('description', None)
            new_ingredients = body.get('ingredients', None)
            new_instruction = body.get('instruction', None)
            new_tea_quantity = body.get('tea_quantity', None)

            tea = Tea.query.filter(Tea.id == id).one_or_none()

            if tea is None:
                abort(404)

            tea.title = new_title
            tea.tea_type = new_tea_type
            tea.code = new_code
            tea.packaging = new_packaging
            tea.price = new_price
            tea.description = new_description
            tea.ingredients = new_ingredients
            tea.instruction = new_instruction
            tea.tea_quantity = new_tea_quantity

            tea.update()

            return jsonify({
                "success": True,
                "updated": tea.format()
            })

        except Exception as e:
            if e.code == 404:
                abort(404, e)
            else:
                abort(422, e)

    @app.route('/tea/<id>', methods=['DELETE'])
    @requires_auth('detele:tea')
    def delete_tea(payload, id):
        try:
            tea = Tea.query.filter(Tea.id == id).one_or_none()

            if tea is None:
                abort(404)

            tea.delete()

            return jsonify({
                "success": True,
                "deleted": id,
                'total_positions': len(Tea.query.all())
            })

        except Exception as e:
            if e.code == 404:
                abort(404, e)
            else:
                abort(422, e)

    @app.route('/catalog', methods=['GET'])
    def get_catalog():
        catalog = Catalog.query.order_by(Catalog.id).all()

        if len(catalog) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'catalog': [catalog_item.format() for catalog_item in catalog],
            'total_catalog_positions': len(catalog)
        })

    @app.route('/catalog', methods=['POST'])
    @requires_auth('post:catalog')
    def create_catalog(payload):
        body = request.get_json()

        new_tea_category = body.get('tea_category', None)
        new_tea_packing = body.get('tea_packing', None)

        try:
            catalog = Catalog(tea_category=new_tea_category, tea_packing=new_tea_packing, tea_list=[])
            catalog.insert()

            return jsonify({
                'success': True,
                'created': catalog.id,
                'total_catalog_positions': len(Catalog.query.all())
            })

        except Exception as e:
            abort(422, e)

    @app.route('/catalog/<id>', methods=['PATCH'])
    @requires_auth('patch:catalog')
    def update_catalog(payload, id):
        try:
            body = request.get_json()

            new_tea_category = body.get('tea_category', None)
            new_tea_packing = body.get('tea_packing', None)

            catalog = Catalog.query.filter(Catalog.id == id).one_or_none()

            if catalog is None:
                abort(404)

            catalog.tea_category = new_tea_category
            catalog.tea_packing = new_tea_packing

            catalog.update()

            return jsonify({
                "success": True,
                "updated": catalog.format()
            })

        except Exception as e:
            if e.code == 404:
                abort(404, e)
            else:
                abort(422, e)

    @app.route('/catalog/<id>', methods=['DELETE'])
    @requires_auth('detele:catalog')
    def delete_catalog(payload, id):
        try:
            catalog = Catalog.query.filter(Catalog.id == id).one_or_none()

            if catalog is None:
                abort(404)

            catalog.delete()

            return jsonify({
                "success": True,
                "deleted": id,
                'total_catalog_positions': len(Catalog.query.all())
            })

        except Exception as e:
            if e.code == 404:
                abort(404, e)
            else:
                abort(422, e)

    @app.route('/order', methods=['GET'])
    @requires_auth('get:order')
    def get_order(payload):
        order = Order.query.order_by(Order.id).all()

        return jsonify({
            'success': True,
            'orders': [order_item.format() for order_item in order],
            'total_orders': len(order)
        })

    @app.route('/order', methods=['POST'])
    @requires_auth('post:order')
    def create_order(payload):
        body = request.get_json()

        new_tea_id = body.get('tea_id', None)
        new_price = body.get('price', None)
        new_quantity = body.get('quantity', None)
        new_total_price = body.get('total_price', None)
        new_client_id = body.get('client_id', None)
        new_status = body.get('status', None)
        new_created_date = body.get('created_date', None)
        new_delivered_date = body.get('delivered_date', None)

        try:
            order = Order(tea_id=new_tea_id, price=new_price, quantity=new_quantity, total_price=new_total_price,
                          client_id=new_client_id, status=new_status, created_date=new_created_date,
                          delivered_date=new_delivered_date)
            order.insert()

            return jsonify({
                'success': True,
                'created': order.id,
                'total_orders': len(Order.query.all())
            })

        except Exception as e:
            abort(422, e)

    @app.route('/order/<id>', methods=['PATCH'])
    @requires_auth('patch:order')
    def update_order(payload, id):
        try:
            body = request.get_json()

            new_tea_id = body.get('tea_id', None)
            new_price = body.get('price', None)
            new_quantity = body.get('quantity', None)
            new_total_price = body.get('total_price', None)
            new_client_id = body.get('client_id', None)
            new_status = body.get('status', None)
            new_created_date = body.get('created_date', None)
            new_delivered_date = body.get('delivered_date', None)

            order = Order.query.filter(Order.id == id).one_or_none()

            if order is None:
                abort(404)

            order.tea_id = new_tea_id
            order.price = new_price
            order.quantity = new_quantity
            order.total_price = new_total_price
            order.client_id = new_client_id
            order.status = new_status
            order.created_date = new_created_date
            order.delivered_date = new_delivered_date

            order.update()

            return jsonify({
                "success": True,
                "updated": order.format()
            })

        except Exception as e:
            if e.code == 404:
                abort(404, e)
            else:
                abort(422, e)

    @app.route('/order/<id>', methods=['DELETE'])
    @requires_auth('detele:order')
    def delete_order(payload, id):
        try:
            order = Order.query.filter(Order.id == id).one_or_none()

            if order is None:
                abort(404)

            order.delete()

            return jsonify({
                "success": True,
                "deleted": id,
                'total_orders': len(Order.query.all())
            })

        except Exception as e:
            if e.code == 404:
                abort(404, e)
            else:
                abort(422, e)

    @app.route('/client', methods=['GET'])
    @requires_auth('get:client')
    def get_client(payload):
        clients = Client.query.order_by(Client.id).all()

        return jsonify({
            'success': True,
            'clients': [client.format() for client in clients],
            'total_clients': len(clients)
        })

    @app.route('/client', methods=['POST'])
    @requires_auth('post:client')
    def create_client(payload):
        body = request.get_json()

        new_name = body.get('name', None)
        new_surname = body.get('surname', None)
        new_email = body.get('email', None)
        new_phone = body.get('phone', None)
        new_address = body.get('address', None)
        new_city = body.get('city', None)
        new_country = body.get('country', None)
        new_postal_code = body.get('postal_code', None)
        new_discount = body.get('discount', None)

        try:
            client = Client(name=new_name, surname=new_surname, email=new_email, phone=new_phone, address=new_address,
                            city=new_city, country=new_country, postal_code=new_postal_code, discount=new_discount,
                            client_orders=[])
            client.insert()

            return jsonify({
                'success': True,
                'created': client.id,
                'total_clients': len(Client.query.all())
            })

        except Exception as e:
            abort(422, e)

    @app.route('/client/<id>', methods=['PATCH'])
    @requires_auth('patch:client')
    def update_client(payload, id):
        try:
            body = request.get_json()

            new_name = body.get('name', None)
            new_surname = body.get('surname', None)
            new_email = body.get('email', None)
            new_phone = body.get('phone', None)
            new_address = body.get('address', None)
            new_city = body.get('city', None)
            new_country = body.get('country', None)
            new_postal_code = body.get('postal_code', None)
            new_discount = body.get('discount', None)

            client = Client.query.filter(Client.id == id).one_or_none()

            if client is None:
                abort(404)

            client.name = new_name
            client.surname = new_surname
            client.email = new_email
            client.phone = new_phone
            client.address = new_address
            client.city = new_city
            client.country = new_country
            client.postal_code = new_postal_code
            client.discount = new_discount

            client.update()

            return jsonify({
                "success": True,
                "updated": client.format()
            })

        except Exception as e:
            if e.code == 404:
                abort(404, e)
            else:
                abort(422, e)

    @app.route('/client/<id>', methods=['DELETE'])
    @requires_auth('detele:client')
    def delete_client(payload, id):
        try:
            client = Client.query.filter(Client.id == id).one_or_none()

            if client is None:
                abort(404)

            client.delete()

            return jsonify({
                "success": True,
                "deleted": id,
                'total_clients': len(Client.query.all())
            })

        except Exception as e:
            if e.code == 404:
                abort(404, e)
            else:
                abort(422, e)

    @app.route('/admin', methods=['GET'])
    @requires_auth('get:admin')
    def get_admin(payload):
        admins = Admin.query.order_by(Admin.id).all()

        return jsonify({
            'success': True,
            'admins': [admin.format() for admin in admins],
            'total_admins': len(admins)
        })

    @app.route('/admin', methods=['POST'])
    @requires_auth('post:admin')
    def create_admin(payload):
        body = request.get_json()

        new_name = body.get('name', None)
        new_surname = body.get('surname', None)
        new_email = body.get('email', None)
        new_phone = body.get('phone', None)
        new_address = body.get('address', None)
        new_city = body.get('city', None)
        new_country = body.get('country', None)
        new_postal_code = body.get('postal_code', None)

        try:
            admin = Admin(name=new_name, surname=new_surname, email=new_email, phone=new_phone, address=new_address,
                          city=new_city, country=new_country, postal_code=new_postal_code)
            admin.insert()

            return jsonify({
                'success': True,
                'created': admin.id,
                'total_admins': len(Admin.query.all())
            })

        except Exception as e:
            abort(422, e)

    @app.route('/admin/<id>', methods=['PATCH'])
    @requires_auth('patch:admin')
    def update_admin(payload, id):
        try:
            body = request.get_json()

            new_name = body.get('name', None)
            new_surname = body.get('surname', None)
            new_email = body.get('email', None)
            new_phone = body.get('phone', None)
            new_address = body.get('address', None)
            new_city = body.get('city', None)
            new_country = body.get('country', None)
            new_postal_code = body.get('postal_code', None)
            new_discount = body.get('discount', None)

            admin = Admin.query.filter(Admin.id == id).one_or_none()

            if admin is None:
                abort(404)

            admin.name = new_name
            admin.surname = new_surname
            admin.email = new_email
            admin.phone = new_phone
            admin.address = new_address
            admin.city = new_city
            admin.country = new_country
            admin.postal_code = new_postal_code
            admin.discount = new_discount

            admin.update()

            return jsonify({
                "success": True,
                "updated": admin.format()
            })

        except Exception as e:
            if e.code == 404:
                abort(404, e)
            else:
                abort(422, e)

    @app.route('/admin/<id>', methods=['DELETE'])
    @requires_auth('detele:admin')
    def delete_admin(payload, id):
        try:
            admin = Admin.query.filter(Admin.id == id).one_or_none()

            if admin is None:
                abort(404)

            admin.delete()

            return jsonify({
                "success": True,
                "deleted": id,
                'total_admins': len(Admin.query.all())
            })

        except Exception as e:
            if e.code == 404:
                abort(404, e)
            else:
                abort(422, e)

    @app.route('/company_contacts', methods=['GET'])
    def get_company_contacts():
        company_contacts = Company.query.order_by(Company.id).all()

        if len(company_contacts) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'company_contacts': [contacts.format() for contacts in company_contacts],
            'total_company_contacts': len(company_contacts)
        })

    @app.route('/company_contacts', methods=['POST'])
    @requires_auth('post:company_contacts')
    def create_company_contacts(payload):
        body = request.get_json()

        new_email = body.get('email', None)
        new_requisites = body.get('requisites', None)
        new_phone = body.get('phone', None)
        new_description = body.get('description', None)

        try:
            company_contacts = Company(email=new_email, requisites=new_requisites, phone=new_phone,
                                       description=new_description)
            company_contacts.insert()

            return jsonify({
                'success': True,
                'created': company_contacts.id,
                'total_company_contacts': len(Company.query.all())
            })

        except Exception as e:
            abort(422, e)

    @app.route('/company_contacts/<id>', methods=['PATCH'])
    @requires_auth('patch:company_contacts')
    def update_company_contacts(payload, id):
        try:
            body = request.get_json()

            new_email = body.get('email', None)
            new_requisites = body.get('requisites', None)
            new_phone = body.get('phone', None)
            new_description = body.get('description', None)

            company_contacts = Company.query.filter(Company.id == id).one_or_none()

            if company_contacts is None:
                abort(404)

            company_contacts.email = new_email
            company_contacts.requisites = new_requisites
            company_contacts.phone = new_phone
            company_contacts.description = new_description

            company_contacts.update()

            return jsonify({
                "success": True,
                "updated": company_contacts.format()
            })

        except Exception as e:
            if e.code == 404:
                abort(404, e)
            else:
                abort(422, e)

    @app.route('/company_contacts/<id>', methods=['DELETE'])
    @requires_auth('detele:company_contacts')
    def delete_company_contacts(payload, id):
        try:
            company_contacts = Company.query.filter(Company.id == id).one_or_none()

            if company_contacts is None:
                abort(404)

            company_contacts.delete()

            return jsonify({
                "success": True,
                "deleted": id,
                'total_company_contacts': len(Company.query.all())
            })

        except Exception as e:
            if e.code == 404:
                abort(404, e)
            else:
                abort(422, e)

    # Error Handling

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": str(error.description) if env == 'DEV' else "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": str(error.description) if env == 'DEV' else "unprocessable"
        }), 422

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": str(error.description) if env == 'DEV' else "method not allowed"
          }), 405

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
          "success": False,
          "error": 500,
          "message": str(error.description) if env == 'DEV' else "internal server error"
          }), 500

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
          "success": False,
          "error": error.status_code,
          "message": error.error['description']
          }), error.status_code

    return app


app = create_app()

# if __name__ == '__main__':
#        app = create_app(env='DEV')
#        app.run(use_reloader=False)
