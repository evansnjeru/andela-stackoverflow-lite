from flask import Flask, jsonify

app = Flask(__name__)

questions = [
        {
            'id': 1,
            'title': u'User question 1',
            'description': u'More info about the question',
            'answered': False,
            'answers': ''
        },
        {
            'id': 2,
            'title': u'User question 2',
            'description': u'More info about the question',
            'answered': False,
            'answers': ''
        },
        {
            'id': 3,
            'title': u'User question 3',
            'description': u'More info about the question',
            'answered': False,
            'answers': ''
        }


    ]

@app.route('/api/v1/auth/signup', methods=['POST'])
def signup():
    return jsonify({'username': 'user', 'password': 'pass'})


@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    return jsonify({'username': 'user', 'password': 'pass'})


@app.route('/api/v1/questions', methods=['GET'])
def fetch_all_questions():
    return jsonify({'questions': questions})


@app.route('/api/v1/questions/<questionId>', methods=['GET'])
def fetch_question(questionId):
    return jsonify({'username': 'user', 'password': 'pass'})


@app.route('/api/v1/questions', methods=['POST'])
def post_question():
    return jsonify({'username': 'user', 'password': 'pass'})


@app.route('/api/v1/questions/<questionId>', methods=['DELETE'])
def delete_question(questionId):
    return jsonify({'username': 'user', 'password': 'pass'})


@app.route('/api/v1/questions/<questionId>/answers', methods=['POST'])
def post_answer(questionId): 
    return jsonify({'username': 'user', 'password': 'pass'})


@app.route('/api/v1/questions/<questionId>/answers/<answerId>', methods=['PUT'])
def mark_preferred_answer(questionId, answerId):
    return jsonify({'username': 'user', 'password': 'pass'})


if __name__ == '__main__':
    app.run(debug=True)
