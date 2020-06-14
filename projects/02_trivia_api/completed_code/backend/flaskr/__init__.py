import sys
sys.path.insert(0, '..')

from flask import Flask, request, abort, jsonify
from sqlalchemy.sql.expression import func
from flask_cors import CORS
import json

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(env='PROD'):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app, env)

  CORS(app, resources={r"/*": {"origins": "*"}})

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, DELETE, OPTIONS')
    return response

  @app.route('/categories', methods=['GET'])
  def get_categories():
    categories = Category.query.order_by(Category.id).all()

    return jsonify({
      'success': True,
      'categories': {category.id: category.type for category in categories}
    })

  @app.route('/questions', methods=['GET'])
  def get_questions():
    questions = Question.query.order_by(Question.id).all()
    current_questions = paginate_questions(request, questions)
    categories = Category.query.order_by(Category.id).all()

    if len(current_questions) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(questions),
      'current_category': None,
      'categories': {category.id: category.type for category in categories}
    })

  def paginate_questions(request, questions):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in questions]
    current_questions = questions[start:end]

    return current_questions

  @app.route('/questions/<id>', methods=['DELETE'])
  def delete_question(id):
    try:
      question = Question.query.filter(Question.id == id).one_or_none()

      if question is None:
        abort(404)

      question.delete()

      return jsonify({
        'success': True,
        'deleted': id,
        'total_questions': len(Question.query.all())
      })

    except Exception as e:
      if e.code == 404:
        abort(404)
      else:
        abort(422)

  @app.route('/questions', methods=['POST'])
  def create_question():
    body = request.get_json()

    new_question = body.get('question', None)
    new_answer = body.get('answer', None)
    new_difficulty = body.get('difficulty', None)
    new_category = body.get('category', None)

    try:
      question = Question(question=new_question, answer=new_answer, difficulty=new_difficulty, category=new_category)
      question.insert()

      return jsonify({
        'success': True,
        'created': question.id,
        'total_questions': len(Question.query.all())
      })

    except:
      abort(422)

  @app.route('/questions/search', methods=['POST'])
  def get_questions_by_search_term():
    body = request.get_json()
    search_term = body.get('searchTerm', None)

    questions = Question.query.filter(Question.question.ilike('%{}%'.format(search_term.lower()))).all()

    return jsonify({
      'success': True,
      'questions': [question.format() for question in questions],
      'total_questions': len(questions),
      'current_category': None
    })

  @app.route('/categories/<id>/questions', methods=['GET'])
  def get_questions_by_category(id):
    questions = Question.query.filter(Question.category == id).all()
    current_questions = paginate_questions(request, questions)

    return jsonify({
      'success': True,
      'questions': current_questions,
      'total_questions': len(questions),
      'current_category': id
    })

  @app.route('/quizzes', methods=['POST'])
  def get_quizz_question():
    body = request.get_json()

    previous_questions = body.get('previous_questions', None)
    quiz_category = body.get('quiz_category', None)

    if quiz_category.get('id') == 0:
      questions = Question.query.filter(Question.id.notin_(previous_questions)).order_by(func.random()).limit(1).all()
    else:
      questions = Question.query.filter(Question.category == quiz_category.get('id'), Question.id.notin_(previous_questions)).order_by(func.random()).limit(1).all()
    questions = [question.format() for question in questions]

    return jsonify({
      'success': True,
      'question': questions[0] if len(questions) > 0 else None
    })

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "Not found"
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

  return app

if __name__ == '__main__':
  app = create_app(env='DEV')
  app.run(use_reloader=False)
    
