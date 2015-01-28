Overview
====

TheRazBot is a simple twitter bot, his job is to remind you about a tweet some time in the future. All you need to do is make a mention to @razpeitia_ and put some offset given in the following format

`[optional tweet text] <HH:MM>`

Tweet example: `@razpeitia_ remind me about this tweet in 00:05`

Requirements
====

* Python 2.7
* RabbitMQ


Setup
====

* Make a virtualenv, you can use virtualenvwrapper.
* Install all the dependencies `pip install -r requirements.txt`
* Set the environment variables:
    * API\_KEY
    * API\_SECRET
    * API\_TOKEN
    * API\_SECRET\_TOKEN
* Run the sender `celery -A sender worker --loglevel=info`, this program will send the tweets.
* Run the listener `python listener.py`, this program will wait for mentions and schedule the response.
