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

# BMX
access_token = '636984272-kV5vKBpz9QJ46UZP8yVmXSulLqLYh55suNinHzmM'
access_token_secret = 'HJWYLX0NE3bdZc2Llyo0CBpc9bHT03mgyiMoSAn70'
consumer_key = 'QSzL0ZJstcIUtEvVv1UgyA'
consumer_secret = 'ljGWKSgxY807frB5uInEmJ506OzI1MZ4eOeoxKZw7g'

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