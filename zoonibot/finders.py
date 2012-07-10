def comments_without_zoonibot_responses(bot, comments):
    zoos = bot.search_comments(['zoonibotans'], since_date='2012-07-10')
    ids = set(z.discussion.id for z in zoos)
    return [c for c in comments if c.discussion.id not in ids]

def find_help_tags(bot):
    comments = list(bot.search_comments(['help']))
    return comments_without_zoonibot_responses(bot, comments)

def find_kepler_planets(bot):
    raise NotImplemented

if __name__ == "__main__":
    from bot import ZooniBot
    from responses import help_response

    bot = ZooniBot(username="zoonibot", api_key="d1b5be9242fb65de9372")

    for t in find_help_tags(bot):
        print t
        print help_response(t)

    bot.find_and_respond(find_help_tags, help_response)
