import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(app=self.app, env='TEST', database_path=self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            'question':  'What is love?',
            'answer': "Oh baby, don't hurt me",
            'difficulty': '100500',
            'category': '2'
        }

        self.invalid_question = {
            'question':  0,
            'answer': 0,
            'difficulty': 0,
            'category': 0
        }

        self.quizz_previous_questions_part = {
          "previous_questions": [22, 20],
           "quiz_category": {"id": "1", "type": "Science"}
        }

        self.quizz_question_output = {
          "id": 21,
          "question": "Who discovered penicillin?",
          "answer": "Alexander Fleming",
          "category": 1,
          "difficulty": 3
        }

        self.quizz_previous_questions_all = {
          "previous_questions": [22, 20, 21],
           "quiz_category": {"id": "1", "type": "Science"}
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertTrue(len(data['categories']))

    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['total_questions'])
        self.assertEqual(data['current_category'], None)
        self.assertTrue(len(data['questions']))
        self.assertTrue(len(data['categories']))

    def test_get_paginated_questions(self):
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['questions']), 10)

    def test_404_page_not_found(self):
        page = self.client().get('/questions?page=100500')
        data = json.loads(page.data)

        self.assertEqual(page.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')

    def test_delete_question(self):
        res = self.client().delete('/questions/2')
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], '2')
        self.assertTrue(data['total_questions'])
        self.assertEqual(question, None)

    def test_404_delete_question_not_found(self):
        res = self.client().delete('/questions/100500')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')


    def test_create_new_question(self):
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_questions'])

    def test_422_create_question_empty(self):
        res = self.client().post('/questions', json=self.invalid_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_405_create_question_not_allowed(self):
        res = self.client().post('/questions/100500', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_get_questions_by_search_term_found(self):
        res = self.client().post('/questions/search', json={'searchTerm': 'what?'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertEqual(data['total_questions'], 2)
        self.assertEqual(data['current_category'], None)

    def test_get_questions_by_search_term_not_found(self):
        res = self.client().post('/questions/search', json={'searchTerm': 'one upon a time'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertFalse(data['questions'])
        self.assertEqual(data['total_questions'], 0)
        self.assertEqual(data['current_category'], None)

    def test_get_questions_by_category_found(self):
        res = self.client().get('/categories/5/questions')
        data = json.loads(res.data)

        questions = Question.query.filter(Question.category == 5).all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertEqual(data['total_questions'], len(questions))
        self.assertEqual(data['current_category'], '5')

    def test_get_questions_by_category_not_found(self):
        res = self.client().get('/categories/0/questions')
        data = json.loads(res.data)

        questions = Question.query.filter(Question.category == 0).all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertFalse(data['questions'])
        self.assertEqual(data['total_questions'], len(questions))
        self.assertEqual(data['current_category'], '0')

    def test_get_quizz_question_found(self):
        res = self.client().post('/quizzes', json=self.quizz_previous_questions_part)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['question'])
        self.assertEqual(data['question'], self.quizz_question_output)

    def test_get_quizz_question_not_found(self):
        res = self.client().post('/quizzes', json=self.quizz_previous_questions_all)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertFalse(data['question'])


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()