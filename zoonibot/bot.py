""" 

"""

# Standard Library
import os,sys
import urllib, urllib2
try:
    # simplejson *is* json, but this works for earlier versions of Python
    import simplejson as json
except ImportError: 
    import json
    
class Bot(object):
    pass
    
class CommentBot(Bot):
    pass
    
class ZooniBot(CommentBot):
    """ The ZooniBot is an automated robot for commenting on
        Zooniverse objects.
    """
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def post(comment):
        """ Post the comment to the Zooniverse by zoonibot """
        pass