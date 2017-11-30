from nose.tools import *
from bin.app import app
from bin.upload import uploadapp
from tests.tools import assert_response

def test_index():
    # Check tha we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status="404")

    # Test our first GET request to /hello
    resp = app.request("/hello")
    assert_response(resp)

    # Make sure default values work for the form
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="ERROR: greet is required.")

    # Test that we get expected values
    data = {'name': 'Wang', 'greet':'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Wang")

def test_upload():
    # Test 404 on the / URL
    resp = uploadapp.request("/")
    assert_response(resp, status="404")

    # Test GET staute 200 on the /upload URL
    resp = uploadapp.request("/upload")
    assert_response(resp)

    # Test upload file
#    data = {}
#    resp = uploadapp.request("/upload", method="POST")
#    assert_response(resp, status="304")

