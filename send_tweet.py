import os

import twitter
# import markov_duplicate

# Available on lab machines
# Otherwise "pip install" into an active virtual env

# Using Python os.environ to get environmental variables
#
# Note: you must run `source secrets.sh` before running
# this file to set required environmental variables.
def post_tweet(tweet): 
    api = twitter.Api(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    # This will print info about credentials to make sure
    # they're correct
    print api.VerifyCredentials()

    # Send a tweet
    status = api.PostUpdate(tweet)
    print status.text

    # If you updated secrets.sh, you can go to your Twitter
    # timeline to see it.
