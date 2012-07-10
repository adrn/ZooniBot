def comments_without_zoonibot_responses(bot, comments):
    zoos = bot.search_comments(['zoonibotans'], since='2012-07-10')
    ids = set(z.discussion.id for z in zoos)
    return [c for c in comments if c.discussion.id not in ids]

def find_help_tags(bot):
    comments = bot.search_comments(['help'])
    return comments_without_zoonibot_responses(bot, comments)

def find_kepler_planets(bot):
    raise NotImplemented
