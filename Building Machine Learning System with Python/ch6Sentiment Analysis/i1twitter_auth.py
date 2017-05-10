import sys
from os import environ


CONSUMER_KEY = environ.get('CONSUMER_KEY')
CONSUMER_SECRET = environ.get('CONSUMER_SECRET')

ACCESS_TOKEN_KEY = environ.get('ACCESS_TOKEN_KEY')
ACCESS_TOKEN_SECRET = environ.get('ACCESS_TOKEN_SECRET')

if CONSUMER_KEY is None or CONSUMER_SECRET is None or ACCESS_TOKEN_KEY is None or ACCESS_TOKEN_SECRET is None:
    print("""\
When doing last code sanity checks for the book, Twitter
was using the API 1.0, which did not require authentication.
With its switch to version 1.1, this has now changed.

It seems that you don't have already created your personal Twitter
access keys and tokens. Please do so at
https://dev.twitter.com/docs/auth/tokens-devtwittercom
and paste the keys/secrets into twitterauth.py

Sorry for the inconvenience,
The authors.""")

    sys.exit(1)