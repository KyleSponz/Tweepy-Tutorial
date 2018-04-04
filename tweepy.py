#This code demonstrates how to login to twitter with their OAUT authentication.
#In Production, you should take other measures to encrypt or otherwise store


import tweepy
import time

# Consumer keys and access tokens, used for OAuth place the keys generated on your account inside the quotations
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Gets list of twitter IDs
ids = []

for page in tweepy.Cursor(api.followers_ids, screen_name="KyleSponable").pages():
    ids.extend(page)
    time.sleep(60)

print(ids)

