import pytest

from application import app


def test_predict():

    with app.test_client() as test_client:
        board = '[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,-1,0,0,1],[-1,-1,-1,-1,0,1,1]]'

        response = test_client.post('/predict', json={
            'player': -1,
            'board': board
        })

        assert response.status_code == 200
