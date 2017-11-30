from nose.tools import *
from bin.gameapp import app, session
from tests.tools import assert_response
import base64
import pickle

def test_game():
    # Test / URL
    resp = app.request("/")
    assert_response(resp, status="200")
    
    # Test hero register
    data = {'heroname': 'HeroOne'}
    resp = app.request("/", method="POST", date=data)
    assert_response(resp, status="303")
    
    # Test /game URL
    resp = app.request("/game")
    assert_response(resp, contains="Central Corridor")

    # Test form POST request
    data = {'action': 'tell a joke'}
    resp = app.request("/game", method="POST", date=data)
    assert_response(resp, status="303")
