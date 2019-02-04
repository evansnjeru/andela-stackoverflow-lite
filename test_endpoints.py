from endpoints import app

all_questions = {
  "questions": [
    {
      "answered": False, 
      "answers": "", 
      "description": "More info about the question", 
      "id": 1, 
      "title": "User question 1"
    }, 
    {
      "answered": False, 
      "answers": "", 
      "description": "More info about the question", 
      "id": 2, 
      "title": "User question 2"
    }, 
    {
      "answered": False, 
      "answers": "", 
      "description": "More info about the question", 
      "id": 3, 
      "title": "User question 3"
    }
  ]
}
 

def test_signup_returns_correct_json_200():
    test_client = app.test_client()
    response = test_client.post('/api/v1/auth/signup')
    assert response.status_code == 200
    assert response.content_type == 'application/json'


def test_login_returns_correct_json_200():
    test_client = app.test_client()
    response = test_client.post('/api/v1/auth/login')
    assert response.status_code == 200
    assert response.content_type == 'application/json'


def test_fetch_all_questions_returns_correct_json_200():
    test_client = app.test_client()
    response = test_client.get('/api/v1/questions')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.json == all_questions
 

def test_fetch_question_returns_correct_json_200():
    test_client = app.test_client()
    response = test_client.get('/api/v1/questions/0')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
 

def test_post_question_returns_correct_json_200():
    test_client = app.test_client()
    response = test_client.post('/api/v1/questions')
    assert response.status_code == 200
    assert response.content_type == 'application/json'


def test_delete_question_returns_correct_json_200():
    test_client = app.test_client()
    response = test_client.delete('/api/v1/questions/0')
    assert response.status_code == 200
    assert response.content_type == 'application/json'


def test_post_answer_returns_correct_json_200():
    test_client = app.test_client()
    response = test_client.post('/api/v1/questions/0/answers')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
 
'''
def test_mark_preferred_answer_returns_correct_json_200():
    test_client = app.test_client()
    response = test_client.post('/ai/v1/questions/0/answers/0')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
'''
