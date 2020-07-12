import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from .api import create_app
from .database.models import setup_db, Tea, Catalog, Order, \
    Client, Admin, Company
from dotenv import load_dotenv


class HilltopTestCase(unittest.TestCase):
    """This class represents the hilltop test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(env='TEST')
        self.client = self.app.test_client
        self.database_name = "hilltop_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432',
                                                       self.database_name)
        setup_db(app=self.app, env='TEST', database_path=self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        # get authorized users
        load_dotenv()
        self.hilltop_adm = os.getenv("HILLTOP_ADMIN")
        self.hilltop_cln = os.getenv("HILLTOP_CLIENT")

        self.new_tea_position = {
            "title": "Hilltop Classic Black Tea",
            "tea_type": "Black Tea",
            "code": "0004",
            "packaging": "100g",
            "price": "1.90",
            "description": "Classic Ceylon Tea",
            "ingredients": "Ceylon Tea leaves",
            "instruction": "Boil it, drink it",
            "tea_quantity": 1000
        }

        self.invalid_tea_position = {
            "title": None,
            "tea_type": None,
            "code": None,
            "packaging": None,
            "price": None,
            "description": None,
            "ingredients": None,
            "instruction": None,
            "tea_quantity": None
        }

        self.update_tea_position = {
            "title": "Hilltop English Breakfast Black Tea",
            "tea_type": "Black Tea",
            "code": "0004",
            "packaging": "200g",
            "price": "2.90",
            "description": "English Breakfast Ceylon Tea",
            "ingredients": "Ceylon Tea leaves",
            "instruction": "Boil it, drink it",
            "tea_quantity": 2000
        }

        self.new_catalog = {
            "tea_category": "Green Tea",
            "tea_packing": "100g"
        }

        self.invalid_catalog = {
            "tea_category": None,
            "tea_packing": None
        }

        self.update_catalog = {
            "tea_category": "Green Fruit Tea",
            "tea_packing": "200g"
        }

        self.new_order = {
            "tea_id": 3,
            "price": "2.70",
            "quantity": 100,
            "total_price": "270",
            "client_id": 2,
            "status": "In Progress",
            "created_date": "Mon, 09 Jul 2020 19:30:00 GMT",
            "delivered_date": None
        }

        self.invalid_order = {
            "tea_id": None,
            "price": None,
            "quantity": None,
            "total_price": None,
            "client_id": None,
            "status": None,
            "created_date": None,
            "delivered_date": None
        }

        self.update_order = {
            "tea_id": 1,
            "price": "2.50",
            "quantity": 1,
            "total_price": "2.50",
            "client_id": 2,
            "status": "Completed",
            "created_date": "Mon, 08 Jul 2020 19:30:00 GMT",
            "delivered_date": "Mon, 09 Jul 2020 19:30:00 GMT"
        }

        self.new_client = {
            "name": "John",
            "surname": "Snow",
            "email": "john.snow@gmail.com",
            "phone": "+371 21112233",
            "address": "Snow street 50 - 99",
            "city": "Wall Town",
            "country": "Winterfell",
            "postal_code": "W-001",
            "discount": 50
        }

        self.invalid_client = {
            "name": None,
            "surname": None,
            "email": None,
            "phone": None,
            "address": None,
            "city": None,
            "country": None,
            "postal_code": None,
            "discount": None
        }

        self.update_client = {
            "name": "John",
            "surname": "Snow",
            "email": "john.snow@gmail.com",
            "phone": "+371 21112233",
            "address": "Snow street 42 - 87",
            "city": "Wall Town",
            "country": "Winterfell",
            "postal_code": "W-001",
            "discount": 90
        }

        self.new_admin = {
            "name": "Cersei",
            "surname": "Lannister",
            "email": "cersei.lannister@gmail.com",
            "phone": "+371 43920134",
            "address": "Casterly Rock street 11 - 191",
            "city": "Casterly Rock",
            "country": "Westeros",
            "postal_code": "WC-001"
        }

        self.invalid_admin = {
            "name": None,
            "surname": None,
            "email": None,
            "phone": None,
            "address": None,
            "city": None,
            "country": None,
            "postal_code": None
        }

        self.update_admin = {
            "name": "Tyrion",
            "surname": "Lannister",
            "email": "tyrion.lannister@gmail.com",
            "phone": "+371 43992131",
            "address": "Casterly Rock street 11 - 191",
            "city": "Casterly Rock",
            "country": "Westeros",
            "postal_code": "WC-001"
        }

        self.new_company_contacts = {

            "email": "noreply@gmail.com",
            "requisites": "LVHABA9002320023230023243",
            "phone": "+399 609090909",
            "description": "Auto-reply email. Hilltop - tea company "
                           "serving finest tea in the world"
        }

        self.invalid_company_contacts = {

            "email": None,
            "requisites": None,
            "phone": None,
            "description": None
        }

        self.update_company_contacts = {

            "email": "autoreply@gmail.com",
            "requisites": "LVHABA9002320023230023243",
            "phone": "+399 609090909",
            "description": "Auto-reply email. Hilltop - tea company "
                           "serving finest tea in the world"
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_tea(self):
        res = self.client().get('/tea')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['tea_list'])
        self.assertTrue(len(data['tea_list']))
        self.assertEqual(data['total_positions'], len(data['tea_list']))

    def test_create_tea(self):
        res = self.client().post('/tea',
                                 json=self.new_tea_position,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_positions'])

    def test_422_create_tea_not_valid(self):
        res = self.client().post('/tea',
                                 json=self.invalid_tea_position,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_405_create_tea_not_allowed(self):
        res = self.client().post('/tea/100500',
                                 json=self.new_tea_position,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_patch_tea(self):
        res = self.client().patch('/tea/2',
                                  json=self.update_tea_position,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

    def test_404_patch_tea_not_found(self):
        res = self.client().patch('/tea/100500',
                                  json=self.update_tea_position,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_422_patch_tea_not_valid(self):
        res = self.client().patch('/tea/2',
                                  json=self.invalid_tea_position,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_tea(self):
        res = self.client().delete('/tea/3',
                                   headers={'Authorization': 'Bearer ' +
                                                             self.hilltop_adm})
        data = json.loads(res.data)

        tea = Tea.query.filter(Tea.id == 3).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], '3')
        self.assertTrue(data['total_positions'])
        self.assertEqual(tea, None)

    def test_404_delete_tea_not_found(self):
        res = self.client().delete('/tea/100500',
                                   headers={'Authorization': 'Bearer ' +
                                                             self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_get_catalog(self):
        res = self.client().get('/catalog')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['catalog'])
        self.assertTrue(len(data['catalog']))
        self.assertEqual(data['total_catalog_positions'], len(data['catalog']))

    def test_create_catalog(self):
        res = self.client().post('/catalog', json=self.new_catalog,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_catalog_positions'])

    def test_422_create_catalog_not_valid(self):
        res = self.client().post('/catalog', json=self.invalid_catalog,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_405_create_catalog_not_allowed(self):
        res = self.client().post('/catalog/100500', json=self.new_catalog,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_patch_catalog(self):
        res = self.client().patch('/catalog/3', json=self.update_catalog,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

    def test_404_patch_catalog_not_found(self):
        res = self.client().patch('/catalog/100500', json=self.update_catalog,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_422_patch_catalog_not_valid(self):
        res = self.client().patch('/catalog/3', json=self.invalid_catalog,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_catalog(self):
        res = self.client().delete('/catalog/4',
                                   headers={'Authorization': 'Bearer ' +
                                                             self.hilltop_adm})
        data = json.loads(res.data)

        catalog = Catalog.query.filter(Catalog.id == 4).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], '4')
        self.assertTrue(data['total_catalog_positions'])
        self.assertEqual(catalog, None)

    def test_404_delete_catalog_not_found(self):
        res = self.client().delete('/catalog/100500',
                                   headers={'Authorization': 'Bearer ' +
                                                             self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_get_order(self):
        res = self.client().get('/order',
                                headers={'Authorization': 'Bearer ' +
                                                          self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['orders'])
        self.assertTrue(len(data['orders']))
        self.assertEqual(data['total_orders'], len(data['orders']))

    def test_create_order(self):
        res = self.client().post('/order', json=self.new_order,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_orders'])

    def test_422_create_order_not_valid(self):
        res = self.client().post('/order', json=self.invalid_order,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_405_create_order_not_allowed(self):
        res = self.client().post('/order/100500', json=self.new_order,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_patch_order(self):
        res = self.client().patch('/order/3', json=self.update_order,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

    def test_404_patch_order_not_found(self):
        res = self.client().patch('/order/100500', json=self.update_order,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_422_patch_order_not_valid(self):
        res = self.client().patch('/order/3', json=self.invalid_order,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_order(self):
        res = self.client().delete('/order/4',
                                   headers={'Authorization': 'Bearer ' +
                                                             self.hilltop_adm})
        data = json.loads(res.data)

        order = Order.query.filter(Order.id == 4).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], '4')
        self.assertTrue(data['total_orders'])
        self.assertEqual(order, None)

    def test_404_delete_order_not_found(self):
        res = self.client().delete('/order/100500',
                                   headers={'Authorization': 'Bearer ' +
                                                             self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_get_client(self):
        res = self.client().get('/client',
                                headers={'Authorization': 'Bearer ' +
                                                          self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['clients'])
        self.assertTrue(len(data['clients']))
        self.assertEqual(data['total_clients'], len(data['clients']))

    def test_create_client(self):
        res = self.client().post('/client', json=self.new_client,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_clients'])

    def test_422_create_client_not_valid(self):
        res = self.client().post('/client', json=self.invalid_client,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_405_create_client_not_allowed(self):
        res = self.client().post('/client/100500', json=self.new_client,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_patch_client(self):
        res = self.client().patch('/client/1', json=self.update_client,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

    def test_404_patch_client_not_found(self):
        res = self.client().patch('/client/100500', json=self.update_client,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_422_patch_client_not_valid(self):
        res = self.client().patch('/client/1', json=self.invalid_client,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_client(self):
        res = self.client().delete('/client/3',
                                   headers={'Authorization': 'Bearer ' +
                                                             self.hilltop_adm})
        data = json.loads(res.data)

        client = Client.query.filter(Client.id == 3).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], '3')
        self.assertTrue(data['total_clients'])
        self.assertEqual(client, None)

    def test_404_delete_client_not_found(self):
        res = self.client().delete('/client/100500',
                                   headers={'Authorization': 'Bearer ' +
                                                             self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_get_admin(self):
        res = self.client().get('/admin',
                                headers={'Authorization': 'Bearer ' +
                                                          self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['admins'])
        self.assertTrue(len(data['admins']))
        self.assertEqual(data['total_admins'], len(data['admins']))

    def test_create_admin(self):
        res = self.client().post('/admin', json=self.new_admin,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_admins'])

    def test_422_create_admin_not_valid(self):
        res = self.client().post('/admin', json=self.invalid_admin,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_405_create_admin_not_allowed(self):
        res = self.client().post('/admin/100500', json=self.new_admin,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_patch_admin(self):
        res = self.client().patch('/admin/1', json=self.update_admin,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

    def test_404_patch_admin_not_found(self):
        res = self.client().patch('/admin/100500', json=self.update_admin,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_422_patch_admin_not_valid(self):
        res = self.client().patch('/admin/1', json=self.invalid_admin,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_admin(self):
        res = self.client().delete('/admin/2',
                                   headers={'Authorization': 'Bearer ' +
                                                             self.hilltop_adm})
        data = json.loads(res.data)

        admin = Admin.query.filter(Admin.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], '2')
        self.assertTrue(data['total_admins'])
        self.assertEqual(admin, None)

    def test_404_delete_admin_not_found(self):
        res = self.client().delete('/admin/100500',
                                   headers={'Authorization': 'Bearer ' +
                                                             self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_get_company_contacts(self):
        res = self.client().get('/company_contacts')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['company_contacts'])
        self.assertTrue(len(data['company_contacts']))
        self.assertEqual(data['total_company_contacts'],
                         len(data['company_contacts']))

    def test_create_company_contacts(self):
        res = self.client().post('/company_contacts',
                                 json=self.new_company_contacts,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_company_contacts'])

    def test_422_create_company_contacts_not_valid(self):
        res = self.client().post('/company_contacts',
                                 json=self.invalid_company_contacts,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_405_create_company_contacts_not_allowed(self):
        res = self.client().post('/company_contacts/100500',
                                 json=self.new_company_contacts,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_patch_company_contacts(self):
        res = self.client().patch('/company_contacts/1',
                                  json=self.update_company_contacts,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])

    def test_404_patch_company_contacts_not_found(self):
        res = self.client().patch('/company_contacts/100500',
                                  json=self.update_company_contacts,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_422_patch_company_contacts_not_valid(self):
        res = self.client().patch('/company_contacts/1',
                                  json=self.invalid_company_contacts,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_company_contacts(self):
        res = self.client().delete('/company_contacts/2',
                                   headers={'Authorization': 'Bearer ' +
                                                             self.hilltop_adm})
        data = json.loads(res.data)

        company_contacts = Company.query.filter(Company.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], '2')
        self.assertTrue(data['total_company_contacts'])
        self.assertEqual(company_contacts, None)

    def test_404_delete_company_contacts_not_found(self):
        res = self.client().delete('/company_contacts/100500',
                                   headers={'Authorization': 'Bearer ' +
                                                             self.hilltop_adm})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_client_get_order(self):
        res = self.client().get('/order',
                                headers={'Authorization': 'Bearer ' +
                                                          self.hilltop_cln})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['orders'])
        self.assertTrue(len(data['orders']))
        self.assertEqual(data['total_orders'], len(data['orders']))

    def test_client_create_order(self):
        res = self.client().post('/order',
                                 json=self.new_order,
                                 headers={'Authorization': 'Bearer ' +
                                                           self.hilltop_cln})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_orders'])

    def test_client_patch_company_contacts(self):
        res = self.client().patch('/company_contacts/1',
                                  json=self.update_company_contacts,
                                  headers={'Authorization': 'Bearer ' +
                                                            self.hilltop_cln})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Permission not found.')

    def test_no_auth_patch_company_contacts(self):
        res = self.client().patch('/company_contacts/1',
                                  json=self.update_company_contacts)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header is expected.')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
