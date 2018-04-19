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

# TreyPitaKoum
access_token = '986715202094813184-UPrbmoyyIK1eDo7H8XEWZcUCsV99JOq'
access_token_secret = 'ni1bBzExCwxoml1Ur8G8KjTlsh9EuMZ99ZfFhcuan51td'
consumer_key = "rHyaOmsKI60MRVHrwtg37MQ99"
consumer_secret = "9dmshplZCCJ6jxbF99VvTCh2lW9O0Vx3njSj8t1zvNdpBd1fI1"

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