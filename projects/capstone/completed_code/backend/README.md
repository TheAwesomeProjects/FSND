# Hilltop Tea Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Environment

It's recommended to work within a virtual environment. This keeps your project dependencies separate and organized. 
Instructions for setting up a virtual environment can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once virtual environment is setup and running, install dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the database operations.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension to handle cross origin requests from the server. 

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Database Setup
With Postgres running, restore a database using the hilltop_test.sql file provided. From the backend folder in terminal run:
```bash
psql hilltop < hilltop_test.sql
```

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.


## Testing
To run the tests, execute:
```
dropdb hilltop_test
createdb hilltop_test
psql hilltop_test < hilltop_test.sql
python test_api.py
```

## Setup authentication

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `post:tea`
    - `patch:tea`
    - `detele:tea`    
    - `post:catalog`    
    - `patch:catalog`    
    - `detele:catalog`   
    - `get:order`   
    - `post:order`   
    - `patch:order`   
    - `detele:order`    
    - `get:client`   
    - `post:client`   
    - `patch:client`   
    - `detele:client`	    
    - `get:admin`   
    - `post:admin`    
    - `patch:admin`	   
    - `detele:admin`	   
    - `post:company_contacts`   
    - `patch:company_contacts`   
    - `detele:company_contacts`

6. Create new roles for:
    - client
        - can `get:order`
        - can `post:order`
    - admin
        - can perform all action
7. Register 2 users - assign the client role to one and admin role to the other.
8. Sign into each account and make note of the JWT.
9. In the  `/src` directory create `.env` file with following environmental variables:

```
export AUTH0_DOMAIN=<Auth0 domain>
export ALGORITHMS=RS256
export API_AUDIENCE=<API audience>
export HILLTOP_ADMIN=<admin JWT token>
export HILLTOP_CLIENT=<client JWT token>
```

    
## Api Reference

    URL: The API is accessible:
        on heroku with https://hilltoptea.herokuapp.com/
        locally with http://127.0.0.1:5000/
    
    Authentication: Bearer Token based authentication using JSON Web Token (JWT)

[View the API_reference.md for Endpoint details.](./API_reference.md)

