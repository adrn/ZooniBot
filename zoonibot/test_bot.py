from bot import ZooniBot
from api import API

class TestZoonibot(object):
    pass

def test_zoonibot():
    api_key = "d1b5be9242fb65de9372"
    url = ""
    
    # Create an API object
    api = API(key=api_key, base_url=url)
    
    # Create a ZooniBot instance 
    zoonibot = ZooniBot(api)
    
    zoonibot.search_comments(tag=["hello"])