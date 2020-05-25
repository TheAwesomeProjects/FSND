# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```


## Api Reference

    URL: At present this app runs only locally and doesn't have a domain name. The backend is accessible with
    http://127.0.0.1:5000/
    
    Authentication: current version of the app doesn't require authentication or API keys

### Endpoints

##### GET ```/categories```
- Returns a success value and dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request arguments: None

Sample: ``` curl http://127.0.0.1:5000/categories ```
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

##### GET ```/questions```
- Returns a success value, list of question objects, total number of questions, dictionary of categories and current category
- Request arguments: None
- Result is paginated, 10 questions per page

Sample: ``` curl http://127.0.0.1:5000/questions ```
```
{
  "success": true,
  "questions": [
    {
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?",
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4
    },
    {
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4
    },
    {
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2
    },
    {
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3
    },
    {
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?",
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1
    },
    {
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?",
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3
    },
    {
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?",
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4
    },
    {
      "id": 12,
      "question": "Who invented Peanut Butter?",
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2
    },
    {
      "id": 13,
      "question": "What is the largest lake in Africa?",
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2
    },
    {
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?",
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3
    }
  ],
  "total_questions": 20,
  "current_category": null,
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
##### GET ```categories/<id>/questions```
- Get questions based on category
- Returns a success value, list of questions in category, total number of questions in category, id of category
- Request arguments: None

Sample: ``` curl http://127.0.0.1:5000/categories/1/questions ```
```
{
  "success": true,
  "questions": [
    {
      "id": 20,
      "question": "What is the heaviest organ in the human body?",
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4
    },
    {
      "id": 21,
      "question": "Who discovered penicillin?",
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3
    },
    {
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?",
      "answer": "Blood",
      "category": 1,
      "difficulty": 4
    },
    {
      "id": 25,
      "question": "ololo?",
      "answer": "trololo",
      "category": 1,
      "difficulty": 500
    }
  ],
  "total_questions": 4,
  "current_category": "1"
}
```

##### POST ```/questions```
- Creates a new question
- Returns a success value, created question id and a total number of questions
- Request arguments: question and answer text, category and difficulty score

Sample: ``` curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d
'{
    "question":  "What is love?",
    "answer": "Oh baby, don't hurt me",
    "difficulty": "100500",
    "category": "2"
}'```

```
{
  "success": true,
  "created": 28,
  "total_questions": 21
}
```

##### POST ```/questions/search```
- Retrieves questions based on a search term
- Returns a success value, list of questions, a total number of questions and current category
- Request arguments: search term

Sample: ``` curl http://127.0.0.1:5000//questions/search -X POST -H "Content-Type: application/json" -d
'{
    "searchTerm":  "olo"
}'```

```
{
  "success": true,
  "questions": [
    {
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?",
      "answer": "Blood",
      "category": 1,
      "difficulty": 4
    },
    {
      "id": 25,
      "question": "ololo?",
      "answer": "trololo",
      "category": 1,
      "difficulty": 500
    }
  ],
  "total_questions": 2,
  "current_category": null
}
```


##### POST ```/quizzes```
- Retrieves a quizz question to play the quiz
- Returns a random question within the given category, being not one of the previous questions
- Request arguments: category and list of previous questions ids

Sample: ``` curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d
'{
  "previous_questions": [22, 20],
   "quiz_category": {"id": "1", "type": "Science"}
}'```

```
{
  "success": true,
  "question": {
    "id": 21,
    "question": "Who discovered penicillin?",
    "answer": "Alexander Fleming",
    "category": 1,
    "difficulty": 3
  }
}
```

## Error Handling

Errors are returned as JSON objects in the following format:

    {
      "success": False,
      "error": 404,
      "message": "Not found"
    }

The API will return four error types when results fail:

    404: Not found
    405: Method Not Allowed
    422: Unprocessable Entity
    500: Internal Server Error
