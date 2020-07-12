### Endpoints

##### GET ```/tea```
- Returns a success value, list of tea positions in the store and a total number of positions
- Request arguments: None

Sample: ``` curl https://hilltoptea.herokuapp.com/tea ```
```
{
  "success": true,
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}
```

##### POST ```/tea```
- Creates a new tea position
- Returns a success value, id of new tea position and a total number of positions in store
- Request arguments: json with new tea position fields filled

Sample: ``` curl https://hilltoptea.herokuapp.com/tea -X POST -H "Content-Type: application/json" -d
'{
    "title": "Hilltop Classic Black Tea",
    "tea_type": "Black Tea",
    "code": "0004",
    "packaging": "100g",
    "price": "1.90",
    "description": "Classic Ceylon Tea",
    "ingredients": "Ceylon Tea leaves",
    "instruction": "Boil it, drink it",
    "tea_quantity": 1000
}'```

```
{
    "success": true,
    "created": 4,
    "total_positions": 4
}
```

##### PATCH ```/tea/<id>```
- Updates existing tea position in the store
- Returns a success value and updated tea position
- Request arguments: json with tea position fields filled

Sample: ``` curl https://hilltoptea.herokuapp.com/tea/4 -X PATCH -H "Content-Type: application/json" -d
'{
    "title": "Hilltop English Breakfast Black Tea",
    "tea_type": "Black Tea",
    "code": "0004",
    "packaging": "200g",
    "price": "2.90",
    "description": "English Breakfast Ceylon Tea",
    "ingredients": "Ceylon Tea leaves",
    "instruction": "Boil it, drink it",
    "tea_quantity": 2000
}'```

```
{
    "success": true,
    "updated": {
        "id": 4,
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
}
```

##### DELETE ```/tea/<id>```
- Deletes existing tea position
- Returns a success value, id of deleted tea position and a total number of positions left in store
- Request arguments: None

Sample: ``` curl https://hilltoptea.herokuapp.com/tea/4 -X DELETE ```

```
{
    "success": true,
    "deleted": "4",
    "total_positions": 3
}
```

##### GET ```/catalog```
- Returns a success value, list of tea categories in catalog, list of tea positions per category and a total number of records in catalog
- Request arguments: None

Sample: ``` curl https://hilltoptea.herokuapp.com/catalog ```
```
{
    "success": true,
    "catalog": [
        {
            "id": 1,
            "tea_category": "Black Classic Tea",
            "tea_packing": "100g",
            "tea_list": [
                {
                    "id": 1,
                    "title": "Hilltop Aristocratic Black Tea. Earl Grey",
                    "tea_type": "Black Tea",
                    "code": "0001",
                    "packaging": "100g",
                    "price": "2.50",
                    "description": "Delicate blend of Ceylon teas, lightly scented with the elegant flavor of bergamot. One of the favorite English teas.",
                    "ingredients": "Black tea flavored with a high dose of bergamot",
                    "instruction": "One teaspoon of tea for 200 ml of boiled water. Wait 4-5 minutes",
                    "tea_quantity": 500
                },
                {
                    "id": 2,
                    "title": "Hilltop Guru Black Tea.",
                    "tea_type": "Black Tea",
                    "code": "0002",
                    "packaging": "100g",
                    "price": "2.70",
                    "description": "Delicate blend of Ceylon teas. Created for true gurus",
                    "ingredients": "Black Guru tea",
                    "instruction": "Boil it, drink it",
                    "tea_quantity": 200
                }
            ]
        },
        {
            "id": 2,
            "tea_category": "Green Classic Tea",
            "tea_packing": "100g",
            "tea_list": []
        },
        {
            "id": 3,
            "tea_category": "Black Fruit Tea",
            "tea_packing": "100g",
            "tea_list": []
        },
        {
            "id": 4,
            "tea_category": "Testing Tea",
            "tea_packing": "1.5gx25",
            "tea_list": [
                {
                    "id": 3,
                    "title": "Hilltop Meditation Black Tea",
                    "tea_type": "Black Tea",
                    "code": "0003",
                    "packaging": "100g",
                    "price": "2.70",
                    "description": "Delicate blend of Ceylon teas. Best for the piece of mind",
                    "ingredients": "Black meditation tea",
                    "instruction": "Boil it, meditate, drink it",
                    "tea_quantity": 300
                }
            ]
        }
    ],
    "total_catalog_positions": 4
}
```

##### POST ```/catalog```
- Adds a new tea category to the catalog
- Returns a success value, id of new catalog record and a total number of records in catalog
- Request arguments: json with new tea category and packing information

Sample: ``` curl https://hilltoptea.herokuapp.com/catalog -X POST -H "Content-Type: application/json" -d
'{
    "tea_category": "Green Fruit Tea",
    "tea_packing": "200g"
}'```

```
{
    "success": true,
    "created": 5,
    "total_catalog_positions": 5
}
```

##### PATCH ```/catalog/<id>```
- Updates existing tea catalog record
- Returns a success value and updated tea catalog record
- Request arguments: json with tea category and packing information

Sample: ``` curl https://hilltoptea.herokuapp.com/catalog/5 -X PATCH -H "Content-Type: application/json" -d
'{
    "tea_category": "Green Sour Sop Tea",
    "tea_packing": "200g"
}'```

```
{
    "success": true,
    "updated": {
        "id": 5,
        "tea_category": "Green Sour Sop Tea",
        "tea_packing": "200g",
        "tea_list": []
    }
}
```

##### DELETE ```/catalog/<id>```
- Deletes existing tea catalog record
- Returns a success value, id of deleted tea catalog record and a total number of records in catalog
- Request arguments: None

Sample: ``` curl https://hilltoptea.herokuapp.com/catalog/5 -X DELETE ```

```
{
    "success": true,
    "deleted": "5",
    "total_catalog_positions": 4
}
```

##### GET ```/order```
- Returns a success value and list of tea orders received by the store
- Request arguments: None

Sample: ``` curl https://hilltoptea.herokuapp.com/order ```
```
{
    "success": true,
    "orders": [
        {
            "id": 1,
            "tea_id": 1,
            "price": "2.50",
            "quantity": 2,
            "total_price": "5",
            "client_id": 1,
            "status": "In Progress",
            "created_date": "Wed, 08 Jul 2020 19:30:00 GMT",
            "delivered_date": null
        },
        {
            "id": 2,
            "tea_id": 2,
            "price": "2.70",
            "quantity": 1,
            "total_price": "2.70",
            "client_id": 1,
            "status": "Completed",
            "created_date": "Wed, 08 Jul 2020 19:30:00 GMT",
            "delivered_date": "Thu, 09 Jul 2020 19:30:00 GMT"
        },
        {
            "id": 3,
            "tea_id": 1,
            "price": "2.50",
            "quantity": 1,
            "total_price": "2.25",
            "client_id": 2,
            "status": "In Progress",
            "created_date": "Wed, 08 Jul 2020 19:30:00 GMT",
            "delivered_date": null
        },
        {
            "id": 4,
            "tea_id": 1,
            "price": "2.50",
            "quantity": 100,
            "total_price": "225",
            "client_id": 2,
            "status": "In Progress",
            "created_date": "Mon, 06 Jul 2020 19:30:00 GMT",
            "delivered_date": null
        }
    ],
    "total_orders": 4
}
```

##### POST ```/order```
- Places a new tea order
- Returns a success value, id of new order and a total number of orders received by the store
- Request arguments: json with new order fields filled

Sample: ``` curl https://hilltoptea.herokuapp.com/order -X POST -H "Content-Type: application/json" -d
'{
    "tea_id": 3,
    "price": "2.70",
    "quantity": 100,
    "total_price": "270",
    "client_id": 2,
    "status": "In Progress",
    "created_date": "Mon, 11 Jul 2020 19:30:00 GMT"
}'```

```
{
    "success": true,
    "created": 5,
    "total_orders": 5
}
```

##### PATCH ```/order/<id>```
- Updates existing tea order
- Returns a success value and updated tea order record
- Request arguments: json with order fields filled

Sample: ``` curl https://hilltoptea.herokuapp.com/order/5 -X PATCH -H "Content-Type: application/json" -d
'{
    "tea_id": 1,
    "price": "2.50",
    "quantity": 1,
    "total_price": "2.50",
    "client_id": 2,
    "status": "Completed",
    "created_date": "Mon, 08 Jul 2020 19:30:00 GMT",
    "delivered_date": "Mon, 09 Jul 2020 19:30:00 GMT"
}'```

```
{
  "success": true,
  "updated": {
    "id": 5,
    "tea_id": 1,
    "price": "2.50",
    "quantity": 1,
    "total_price": "2.50",
    "client_id": 2,
    "status": "Completed",
    "created_date": "Wed, 08 Jul 2020 19:30:00 GMT",
    "delivered_date": "Thu, 09 Jul 2020 19:30:00 GMT"
  }
}
```

##### DELETE ```/order/<id>```
- Deletes existing order record
- Returns a success value, id of deleted order record and a total number of orders in the store
- Request arguments: None

Sample: ``` curl https://hilltoptea.herokuapp.com/order/5 -X DELETE ```

```
{
    "success": true,
    "deleted": "5",
    "total_orders": 4
}
```

##### GET ```/client```
- Returns a success value, list of clients, client orders and a total number of clients in the store
- Request arguments: None

Sample: ``` curl https://hilltoptea.herokuapp.com/client ```
```
{
    "success": true,
    "clients": [
        {
            "id": 1,
            "name": "Taylor",
            "surname": "Swift",
            "email": "taylor.swift@gmail.com",
            "phone": "+392 60203109",
            "address": "Swift street 11 - 94",
            "city": "California",
            "country": "USA",
            "postal_code": "TS-001",
            "discount": 0,
            "client_orders": [
                {
                    "id": 1,
                    "tea_id": 1,
                    "price": "2.50",
                    "quantity": 2,
                    "total_price": "5",
                    "status": "In Progress",
                    "created_date": "Wed, 08 Jul 2020 19:30:00 GMT",
                    "delivered_date": null
                },
                {
                    "id": 2,
                    "tea_id": 2,
                    "price": "2.70",
                    "quantity": 1,
                    "total_price": "2.70",
                    "status": "Completed",
                    "created_date": "Wed, 08 Jul 2020 19:30:00 GMT",
                    "delivered_date": "Thu, 09 Jul 2020 19:30:00 GMT"
                }
            ]
        },
        {
            "id": 2,
            "name": "Fedor",
            "surname": "Godhand",
            "email": "fedor.godhand@gmail.com",
            "phone": "+371 21012102",
            "address": "Godhand street 1 - 12",
            "city": "Riga",
            "country": "Latvia",
            "postal_code": "LV-002",
            "discount": 10,
            "client_orders": [
                {
                    "id": 3,
                    "tea_id": 1,
                    "price": "2.50",
                    "quantity": 1,
                    "total_price": "2.25",
                    "status": "In Progress",
                    "created_date": "Wed, 08 Jul 2020 19:30:00 GMT",
                    "delivered_date": null
                },
                {
                    "id": 4,
                    "tea_id": 1,
                    "price": "2.50",
                    "quantity": 100,
                    "total_price": "225",
                    "status": "In Progress",
                    "created_date": "Mon, 06 Jul 2020 19:30:00 GMT",
                    "delivered_date": null
                }
            ]
        },
        {
            "id": 3,
            "name": "TEST",
            "surname": "Client",
            "email": "test.test@gmail.com",
            "phone": "+371 20102010",
            "address": "Test street 1 - 1",
            "city": "Riga",
            "country": "Latvia",
            "postal_code": "LV-003",
            "discount": 0,
            "client_orders": []
        }
    ],
    "total_clients": 3
}
```

##### POST ```/client```
- Creates new online store client
- Returns a success value, id of new client and a total number of clients in the store
- Request arguments: json with new client fields filled

Sample: ``` curl https://hilltoptea.herokuapp.com/client -X POST -H "Content-Type: application/json" -d
'{
    "name": "John",
    "surname": "Snow",
    "email": "john.snow@gmail.com",
    "phone": "+371 21112233",
    "address": "Snow street 50 - 99",
    "city": "Wall Town",
    "country": "Winterfell",
    "postal_code": "W-001",
    "discount": 50
}'```

```
{
    "success": true,
    "created": 4,
    "total_clients": 4
}
```

##### PATCH ```/client/<id>```
- Updates existing client information
- Returns a success value and updated client record
- Request arguments: json with client fields filled

Sample: ``` curl https://hilltoptea.herokuapp.com/client/4 -X PATCH -H "Content-Type: application/json" -d
'{
    "name": "John",
    "surname": "Snow",
    "email": "john.snow@gmail.com",
    "phone": "+371 21112233",
    "address": "Snow street 42 - 87",
    "city": "Wall Town",
    "country": "Winterfell",
    "postal_code": "W-001",
    "discount": 90
}'```

```
{
    "success": true,
    "updated": {
        "id": 4,
        "name": "John",
        "surname": "Snow",
        "email": "john.snow@gmail.com",
        "phone": "+371 21112233",
        "address": "Snow street 42 - 87",
        "city": "Wall Town",
        "country": "Winterfell",
        "postal_code": "W-001",
        "discount": 90,
        "client_orders": []
    }
}
```

##### DELETE ```/client/<id>```
- Deletes existing client record
- Returns a success value, id of deleted client record and a total number of clients in the store
- Request arguments: None

Sample: ``` curl https://hilltoptea.herokuapp.com/client/4 -X DELETE ```

```
{
    "success": true,
    "deleted": "4",
    "total_clients": 3
}
```

##### GET ```/admin```
- Returns a success value, list of admins and a total number of admins in the store
- Request arguments: None

Sample: ``` curl https://hilltoptea.herokuapp.com/admin ```
```
{
    "success": true,
    "admins": [
        {
            "id": 1,
            "name": "Admin",
            "surname": "The Great",
            "email": "admin.great@gmail.com",
            "phone": "+371 20002040",
            "address": "The Great street 11 - 244",
            "city": "Riga",
            "country": "Latvia",
            "postal_code": "LV-003"
        },
        {
            "id": 2,
            "name": "Admin",
            "surname": "Not So Great",
            "email": "admin.notgreat@gmail.com",
            "phone": "+371 29392009",
            "address": "Not So Great street 19 - 192",
            "city": "Riga",
            "country": "Latvia",
            "postal_code": "LV-008"
        }
    ],
    "total_admins": 2
}
```

##### POST ```/admin```
- Creates new online store admin
- Returns a success value, id of new admin and a total number of admins in the store
- Request arguments: json with new admin fields filled

Sample: ``` curl https://hilltoptea.herokuapp.com/admin -X POST -H "Content-Type: application/json" -d
'{
    "name": "Cersei",
    "surname": "Lannister",
    "email": "cersei.lannister@gmail.com",
    "phone": "+371 43920134",
    "address": "Casterly Rock street 11 - 191",
    "city": "Casterly Rock",
    "country": "Westeros",
    "postal_code": "WC-001"
}'```

```
{
    "success": true,
    "created": 3,
    "total_admins": 3
}
```

##### PATCH ```/admin/<id>```
- Updates existing admin information
- Returns a success value and updated admin record
- Request arguments: json with admin fields filled

Sample: ``` curl https://hilltoptea.herokuapp.com/admin/3 -X PATCH -H "Content-Type: application/json" -d
'{
    "name": "Tyrion",
    "surname": "Lannister",
    "email": "tyrion.lannister@gmail.com",
    "phone": "+371 43992131",
    "address": "Casterly Rock street 11 - 191",
    "city": "Casterly Rock",
    "country": "Westeros",
    "postal_code": "WC-001"
}'```

```
{
    "success": true,
    "updated": {
        "id": 3,
        "name": "Tyrion",
        "surname": "Lannister",
        "email": "tyrion.lannister@gmail.com",
        "phone": "+371 43992131",
        "address": "Casterly Rock street 11 - 191",
        "city": "Casterly Rock",
        "country": "Westeros",
        "postal_code": "WC-001"
    }
}
```

##### DELETE ```/admin/<id>```
- Deletes existing admin record
- Returns a success value, id of deleted admin record and a total number of admins in the store
- Request arguments: None

Sample: ``` curl https://hilltoptea.herokuapp.com/admin/3 -X DELETE ```

```
{
    "success": true,
    "deleted": "3",
    "total_admins": 2
}
```

##### GET ```/company_contacts```
- Returns a success value, contact information records and a total number of records
- Request arguments: None

Sample: ``` curl https://hilltoptea.herokuapp.com/company_contacts ```
```
{
    "success": true,
    "company_contacts": [
        {
            "id": 1,
            "email": "hilltop@gmail.com",
            "requisites": "LVHABA000232002323002323",
            "phone": "+371 209090919",
            "description": "Hilltop - tea company serving finest tea in the world"
        },
        {
            "id": 2,
            "email": "reception@gmail.com",
            "requisites": "LVHABA000232002323002323",
            "phone": "+371 20293921",
            "description": "Company reception address. Hilltop - tea company serving finest tea in the world"
        }
    ],
    "total_company_contacts": 2
}
```

##### POST ```/company_contacts```
- Creates new contact information record
- Returns a success value, id of contact information record and a total number of records
- Request arguments: json with new contact information record fields filled

Sample: ``` curl https://hilltoptea.herokuapp.com/company_contacts -X POST -H "Content-Type: application/json" -d
'{
    "email": "noreply@gmail.com",
    "requisites": "LVHABA9002320023230023243",
    "phone": "+399 609090909",
    "description": "Auto-reply email. Hilltop - tea company serving finest tea in the world"
}'```

```
{
    "success": true,
    "created": 3,
    "total_company_contacts": 3
}
```

##### PATCH ```/company_contacts/<id>```
- Updates existing contact information record
- Returns a success value and updated contact information record
- Request arguments: json with contact information record fields filled

Sample: ``` curl https://hilltoptea.herokuapp.com/company_contacts/3 -X PATCH -H "Content-Type: application/json" -d
'{
    "email": "autoreply@gmail.com",
    "requisites": "LVHABA9002320023230023243",
    "phone": "+399 609090909",
    "description": "Auto-reply email. Hilltop - tea company serving finest tea in the world"
}'```

```
{
    "success": true,
    "updated": {
        "id": 3,
        "email": "autoreply@gmail.com",
        "requisites": "LVHABA9002320023230023243",
        "phone": "+399 609090909",
        "description": "Auto-reply email. Hilltop - tea company serving finest tea in the world"
    }
}
```

##### DELETE ```/company_contacts/<id>```
- Deletes existing contact information record
- Returns a success value, id of deleted contact information record and a total number of contact records left
- Request arguments: None

Sample: ``` curl https://hilltoptea.herokuapp.com/company_contacts/3 -X DELETE ```

```
{
    "success": true,
    "deleted": "3",
    "total_company_contacts": 2
}
```

## Error Handling

Errors are returned as JSON objects in the following format:

    {
      "success": False,
      "error": 404,
      "message": "method not allowed"
    }

The API will return four error types when results fail:

    404: resource not found
    405: method not allowed
    422: unprocessable
    500: internal server error
