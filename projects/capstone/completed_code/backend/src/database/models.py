import os
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, UniqueConstraint
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# get env variables
load_dotenv()
database_path = os.getenv("DATABASE_URL")

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, env, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['JSON_SORT_KEYS'] = False

    # env config
    if env == 'DEV':
        app.config["DEBUG"] = True
        app.config["ENV"] = 'development'
    elif env == 'TEST':
        app.config['TESTING'] = True
        app.config["ENV"] = 'testing'
    else:
        app.config["ENV"] = 'production'

    db.app = app
    db.init_app(app)

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


tea_catalog = db.Table(
    'tea_catalog',
    Column('catalog_id', Integer, ForeignKey('catalog.id'), primary_key=True),
    Column('tea_id', Integer, ForeignKey('tea.id'), primary_key=True)
)


class Tea(db.Model):
    __tablename__ = 'tea'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    tea_type = Column(String, nullable=False)
    code = Column(String, nullable=False)
    packaging = Column(String, nullable=False)
    price = Column(String, nullable=False)
    description = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)
    instruction = Column(String, nullable=True)
    tea_quantity = Column(Integer, nullable=False)  # available quantity in the shop
    tea_orders = db.relationship('Order', backref=db.backref('tea', lazy=True))

    __table_args__ = (
        UniqueConstraint('title', name='tea_title_unique_key'),
    )

    def __init__(self, title, tea_type, code, packaging, price, description, ingredients, instruction, tea_quantity):
        self.title = title
        self.tea_type = tea_type
        self.code = code
        self.packaging = packaging
        self.price = price
        self.description = description
        self.ingredients = ingredients
        self.instruction = instruction
        self.tea_quantity = tea_quantity

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'tea_type': self.tea_type,
            'code': self.code,
            'packaging': self.packaging,
            'price': self.price,
            'description': self.description,
            'ingredients': self.ingredients,
            'instruction': self.instruction,
            'tea_quantity': self.tea_quantity
        }


class Catalog(db.Model):
    __tablename__ = 'catalog'

    id = Column(Integer, primary_key=True)
    tea_category = Column(String, nullable=False)
    tea_packing = Column(String, nullable=False)
    tea_list = db.relationship('Tea', secondary=tea_catalog, backref=db.backref('catalog', lazy=True))

    def __init__(self, tea_category, tea_packing, tea_list):
        self.tea_category = tea_category
        self.tea_packing = tea_packing
        self.tea_list = tea_list

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'tea_category': self.tea_category,
            'tea_packing': self.tea_packing,
            'tea_list': [{
                'id': tea.id,
                'title': tea.title,
                'tea_type': tea.tea_type,
                'code': tea.code,
                'packaging': tea.packaging,
                'price': tea.price,
                'description': tea.description,
                'ingredients': tea.ingredients,
                'instruction': tea.instruction,
                'tea_quantity': tea.tea_quantity
            } for tea in self.tea_list]
        }


class User(db.Model):
    __abstract__ = True

    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)

    def __init__(self, name, surname, email, phone, address, city, country, postal_code):
        self.name = name
        self.surname = surname
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.country = country
        self.postal_code = postal_code


class Client(User):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    discount = Column(Integer, nullable=True)
    client_orders = db.relationship('Order', backref=db.backref('client', lazy=True))

    def __init__(self, name, surname, email, phone, address, city, country, postal_code, discount, client_orders):
        super().__init__(name, surname, email, phone, address, city, country, postal_code)
        self.discount = discount
        self.client_orders = client_orders

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'city': self.city,
            'country': self.country,
            'postal_code': self.postal_code,
            'discount': self.discount,
            'client_orders': [{
                'id': order.id,
                'tea_id': order.tea_id,
                'price': order.price,
                'quantity': order.quantity,
                'total_price': order.total_price,
                'status': order.status,
                'created_date': order.created_date,
                'delivered_date': order.delivered_date
            } for order in self.client_orders]
        }


class Admin(User):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True)

    def __init__(self, name, surname, email, phone, address, city, country, postal_code):
        super().__init__(name, surname, email, phone, address, city, country, postal_code)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.email,
            'phone': self.phone,
            'address': self.address,
            'city': self.city,
            'country': self.country,
            'postal_code': self.postal_code
        }


class Order(db.Model):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    tea_id = Column(Integer, ForeignKey('tea.id'), primary_key=False)
    price = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(String, nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), primary_key=False)
    status = Column(String, nullable=False)
    created_date = Column(DateTime(timezone=False), nullable=False)
    delivered_date = Column(DateTime(timezone=False), nullable=True)

    def __init__(self, tea_id, price, quantity, total_price, client_id, status, created_date, delivered_date):
        self.tea_id = tea_id
        self.price = price
        self.quantity = quantity
        self.total_price = total_price
        self.client_id = client_id
        self.status = status
        self.created_date = created_date
        self.delivered_date = delivered_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'tea_id': self.tea_id,
            'price': self.price,
            'quantity': self.quantity,
            'total_price': self.total_price,
            'client_id': self.client_id,
            'status': self.status,
            'created_date': self.created_date,
            'delivered_date': self.delivered_date
        }


class Company(db.Model):
    __tablename__ = 'company_contacts'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    requisites = Column(String, nullable=False)
    phone = Column(String, nullable=True)
    description = Column(String, nullable=True)

    __table_args__ = (
        UniqueConstraint('email', name='company_email_key'),
    )

    def __init__(self, email, requisites, phone, description):
        self.email = email
        self.requisites = requisites
        self.phone = phone
        self.description = description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'email': self.email,
            'requisites': self.requisites,
            'phone': self.phone,
            'description': self.description
        }
