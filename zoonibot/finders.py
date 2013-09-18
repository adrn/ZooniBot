""" TODO: Describe this module! 
    TODO: All of these functions use the default "since_date", when in fact they should decide this somehow?
"""

# Standard library
import os
import re

def comment_is_a_question(comment):
    match = (comment.comment.body[-1]) == "?"
    if match:
        return True
    else:
        return False

def comment_contains_words(comment, wordlist=[]):
    hits = {}
    for w in wordlist:
		hits[w] = re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search(comment.comment.body)
    return hits

def comment_contains_at_least_one(comment, wordlist=[]):
    hits = comment_contains_words(comment,wordlist)
    for hit in hits.values():
        if hit:
            return comment
    return None

def comment_contains_all(comment, wordlist=[]):
	hits = comment_contains_words(comment,wordlist)
	for w in wordlist:
		if w==None:
			return None
	return comment
	
def comments_without_zoonibot_responses(bot, comments):
    zoos = bot.search_comments(['zoonibotans'], since_date='2012-07-10')
    ids = set(z.discussion.id for z in zoos)
    return [c for c in comments if c.discussion.id not in ids]

def find_help_tags(bot, since="2013-09-17"):
    # TODO: since here should also default to yesterday?
    comments = list(bot.search_comments(['help'], since_date=since))
    return comments_without_zoonibot_responses(bot, comments)

def find_test_tags(bot, since="2012-07-10"):
		comments = list(bot.search_comments(['booya'], since_date=since))
		comments2= comments_without_zoonibot_responses(bot, comments)
		words = ['flibble']
		results = []
		for c in comments2: 
			x = comment_contains_at_least_one(c,words)
			if x:
				results.append(c)
		return results

def find_transit_queries(bot, since='2013-09-17'):
    comments = list(bot.search_comments(['transit', 'transits'], since_date=since))
    comments2 = comments_without_zoonibot_responses(bot,comments)
    results = []
    for c in comments2:
        if comment_is_a_question(c):
            results.append(c)
    return results

def find_gam_dor_hash(bot, since='2013-09-17'):
	comments = list(bot.search_comments(['gdor'], since_date=since))
	return comments_without_zoonibot_responses(bot, comments)		

def find_gam_dor_text(bot, since='2013-09-05'):
		comments = list(bot.search_comments([''], since_date=since))
		comments2= comments_without_zoonibot_responses(bot, comments)
		words = ['gamma','doradis']
		results = []
		for c in comments2: 
			x = comment_contains_all(c,words)
			if x:
				results.append(c)
		return results

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

def find_zoonibot_tag(bot, since="2012-07-10"):
    comments = list(bot.search_comments(['zoonibot'], since_date=since))
    return comments_without_zoonibot_responses(bot, comments)

