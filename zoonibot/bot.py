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