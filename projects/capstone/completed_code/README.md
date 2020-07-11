# Hilltop Tea Shop

Hilltop has decided to popularize the brand on the Baltic countries market and for that reason require an official online shop with 
international delivery by post service to the client's specified location.

The Hilltop online shop contain following sections:

1) Tea catalog with all the positions available in the store
2) Company contacts information
3) Option for public users to view available tea in the store and company information
4) Option for users to register and place orders
5) Option for the online shop administrators to modify tea, orders, company and user information

## About the Stack

The application is designed with some key functional areas:

### Backend

The `./backend` directory contains Flask application with SQLAlchemy module. The main python module is apy.py where 
all the endpoints used in application are specified. api.py references models.py for DB and SQLAlchemy setup. Auth0 is used 
for authentication.


[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a React frontend to consume the data from the Flask server. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

`FRONTEND AND TEA DELIVERY ARE NOT INCLUDED IN THE FIRST APPLICATION VERSION` 
