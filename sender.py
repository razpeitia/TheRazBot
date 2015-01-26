import tweepy
import settings
import re
from celery import Celery

auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET)
auth.set_access_token(settings.API_TOKEN, settings.API_SECRET_TOKEN)
api = tweepy.API(auth)

app = Celery('sender', broker='amqp://guest@localhost//')

@app.task
def schedule_status(_id, status):
    api.update_status(status, in_reply_to_status_id=_id)
