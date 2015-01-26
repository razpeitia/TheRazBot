import tweepy
import settings
import re
from sender import schedule_status

auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET)
auth.set_access_token(settings.API_TOKEN, settings.API_SECRET_TOKEN)
api = tweepy.API(auth)

class ReplyListener(tweepy.StreamListener):
    _pattern = re.compile(r'.*(\d{1,2}):(\d{1,2})$')

    def _parse(self, text):
        match = self._pattern.match(text)
        if match:
            hours, minutes = map(int, match.groups())
            return (hours * 60 + minutes) * 60

    def on_status(self, status):
        # There is a status tweeted tagging the user
        username = status.author.screen_name
        offset = self._parse(status.text)

        if offset is None:
            data = {
                "username": username,
            }

            # Send a error message
            message = "@%(username)s Syntax Error, usage: MESSAGE hh:mm" % data
            api.update_status(message, in_reply_to_status_id=status.id)
        else:
            data = {
                "username": username,
                "offset": offset,
            }

            # Schedule an status update in the future
            message = "@%(username)s remember this tweet" % data
            schedule_status.apply_async((status.id, message), countdown=offset)

            # Inform the user that it has been schedule
            message = "@%(username)s scheduled to run in %(offset)s" % data
            api.update_status(message, in_reply_to_status_id=status.id)

        return True 

    def on_error(self, statusCode):
        # There was a listener error
        print "There was a listener error with the code", statusCode 
        return True

    def on_timeout(self):
        # There was a listener timeout
        print "There was a listener timeout"
        return True

listener = tweepy.streaming.Stream(auth, ReplyListener())
# Listen for a response to the user
listener.filter(track=["@" + api.me().screen_name])
