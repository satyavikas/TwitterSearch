# -*- coding: utf-8 -*-
'''
Created on Apr 18, 2018

@author: smanda
'''

import json
import sys
import traceback
import twitter
from src.tweet_transformer import transform_tweet
from src.solr_indexer import index_to_solr

# Michael
access_token = '986760717876506626-Hr2lP61w1Bd51SIdj4s4cB2354Bewxn'
access_token_secret = 'tU8uYYrRktgMQuP5eSfX2JFAPkBWcx4bcV0qF5SxlZARw'
consumer_key = "lPAnK5vlWiwlndUfinNcgEx03"
consumer_secret = "sTFwfqbDIxvG4mdpXPDxqd8Jtc4BDiZPDFoOtE4us8V7iR3ckh"

api = twitter.Api(consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret)

results = api.GetStreamFilter(track=["Donald Trump", "India","F-1", "H1B", "H1-B", "Immigration"])

for tweet in results:
    try:
        transformed_tweet = transform_tweet(tweet)
        index_to_solr(transformed_tweet)
    except Exception as e:
        print(e)
        traceback.print_exc
        sys.exit()
