""" TODO: Describe this module! 
    TODO: All of these functions use the default "since_date", when in fact they should decide this somehow?
"""

# Standard library
import os
import re

def comments_without_zoonibot_responses(bot, comments):
    zoos = bot.search_comments(['zoonibotans'], since_date='2012-07-10')
    ids = set(z.discussion.id for z in zoos)
    return [c for c in comments if c.discussion.id not in ids]

def find_help_tags(bot, since="2012-07-10"):
    # TODO: since here should also default to yesterday?
    comments = list(bot.search_comments(['help'], since_date=since))
    return comments_without_zoonibot_responses(bot, comments)

def find_test_tags(bot, since="2012-07-10"):
	    # TODO: since here should also default to yesterday?
	    comments = list(bot.search_comments(['ZoonibotZoonibotZoonibot'], since_date=since))
	    return comments_without_zoonibot_responses(bot, comments)

def find_planet_binaries(bot, since="2012-07-10"):
    # TODO: since here should also default to yesterday?
    
    pattr = re.compile("(.*zoonibot)*")
    proj_path = pattr.search(__file__).groups()[0]

    with open(os.path.join(proj_path,"_data/zoonibotebs.csv"), "r") as f:
        known_ebs = [x.strip() for x in f.readlines()]
        
    planet_comments = bot.search_comments(['planet'], since_date=since)
    transit_comments = bot.search_comments(['transit'], since_date=since)
    
    respond_to = list()
    for zooni_comment in planet_comments:
        if zooni_comment.light_curve.zooniverse_id in known_ebs and zooni_comment not in respond_to:
            respond_to.append(zooni_comment)
    
    already_added_ids = [c.light_curve.zooniverse_id for c in respond_to]
    for zooni_comment in transit_comments:
        if zooni_comment.light_curve.zooniverse_id in known_ebs and zooni_comment.light_curve.zooniverse_id not in already_added_ids:
            respond_to.append(zooni_comment)
    
    return comments_without_zoonibot_responses(bot, respond_to)

def find_kepler_planets(bot):
    raise NotImplemented

