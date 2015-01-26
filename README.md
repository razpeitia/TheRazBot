Introduction
====

TheRazBot is a simple twitter bot, his job is remaind you some tweet in the future. All you need to do is make a mention to @razpeitia_ and put some offset given in the format HH:MM (hours:minutes).


Requirements
====

* Python 2.7
* RabbitMQ


Setup
====

* Make a virtualenv, you can use virtualenvwrapper.
* Install all the dependencies `pip install requirements.txt`
* Set the environment variables:
    * API\_KEY
    * API\_SECRET
    * API\_TOKEN
    * API\_SECRET\_TOKEN
* Run the sender `celery -A sender worker --loglevel=info`, this program will send the tweets.
* Run the listener `python listener.py`, this program will wait for mentions and schedule the response.
