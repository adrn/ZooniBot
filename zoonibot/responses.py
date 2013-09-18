""" TODO: Describe this module! 
"""

# Standard Library
import copy

# Project
import entry

def response_packer(old_comment, response):
    result = copy.deepcopy(old_comment)
    result.comment = response
    return result

def yourmom_response(zooniverse_comment):
    """ Returns a ZooniverseComment object containing a canned response
        to an input ZooniverseComment object.
    """
    tag_list_str = ", ".join(zooniverse_comment.comment.tags)
    response_comment = entry.Comment(body="Uh, your mom posted about {0}.".format(tag_list_str))

    return response_packer(zooniverse_comment, response_comment)

def help_response(zooniverse_comment):
    """ TODO: describe! """
    response_comment = entry.Comment(body="""Hiya Have you tried our [tutorial video](http://www.planethunters.org/site_guide#video "") and [site guide](http://www.planethunters.org/site_guide "") - they are both good resources for new people #zoonibotans""")
    return response_packer(zooniverse_comment, response_comment)

def test_response(zooniverse_comment):
	    """ TODO: describe! """
	    response_comment = entry.Comment(body="""I daresay, Keep Calm and Classify On! #zoonibotans""")
	    return response_packer(zooniverse_comment, response_comment)

def planet_binaries_response(zooniverse_comment):
    """ Canned response to handle cases where a light curve is flagged as both
        a planet *and* an eclipsing binary or a transit *and* an eclipsing binary.
    """ 
    response_comment = entry.Comment(body="You said there was a planet transit but this is a known #eclipsingbinary where there is a star moving in front of another star. #zoonibotans")
    return response_packer(zooniverse_comment, response_comment)
    
def zoonibot_response(zooniverse_comment):
    """ TODO: describe! """
    response_comment = entry.Comment(body="""You called? I'm here to help! Perhaps you want to know about [I am Bender please insert girder]?""")
    return response_packer(zooniverse_comment, response_comment)

def transit_response(zooniverse_comment, bodytext=""):
    response_comment = entry.Comment(body=bodytext)
    return response_packer(zooniverse_comment, response_comment)

def gammador_response(zooniverse_comment):
	response_comment = entry.Comment(body="""I am Zoonibot. The people who `helpfully' programmed me have asked me to say at this juncture that a Gamma Doradus variable is a type of star that undergoes periodic variations in brightness. There's more info here, http://en.wikipedia.org/wiki/Gamma_Doradus_variable , for what it's worth. #zoonibotans""")
	return response_packer(zooniverse_comment, response_comment)