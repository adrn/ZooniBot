from bot import ZooniBot
from api import API

class TestZoonibot(object):
    pass

def test_zoonibot():
    api_key = "d1b5be9242fb65de9372"
    url = ""

    # Create an API object
    api = API('user', 'key')

    # Create a ZooniBot instance
    zoonibot = ZooniBot(api)
