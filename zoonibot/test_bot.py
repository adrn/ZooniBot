from bot import ZooniBot
import entry

class TestZoonibot(object):
    
    def test_post(self):
        """ WARNING! This *actually* creates a post! """
        
        # Create a ZooniBot instance 
        zoonibot = ZooniBot(username="zoonibot", \
                            api_key="d1b5be9242fb65de9372")
        
        # Create a test ZooniverseComment
        comment = entry.Comment(body="Hello world, I am the semi-sentient #ZooniBot")
        discussion = entry.Discussion(id="4f64be222fa49878e700b2e6")
        
        zooniverse_comment = entry.ZooniverseComment(comment=comment, discussion=discussion)
        zoonibot.post(zooniverse_comment)
        