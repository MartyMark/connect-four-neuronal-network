import json

from src import create_app


def test_predict():
    app = create_app()

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        print("test")
        # response = test_client.post('/predict', json.dumps({
        #    'player': -1,
        #    'board': '[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,-1,0,0,1],[-1,-1,-1,-1,0,1,1]]'
        # }))

        # response = test_client.get('/test')

        # assert response.status_code == 200
