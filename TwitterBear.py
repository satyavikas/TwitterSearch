# -*- coding: utf-8 -*-
'''
Created on Apr 18, 2018

@author: smanda
'''

import json
import sys
import traceback

import twitter

from solr_indexer import index_to_solr
from tweet_transformer import transform_tweet

# BMX:
'''
access_token = '636984272-kV5vKBpz9QJ46UZP8yVmXSulLqLYh55suNinHzmM'
access_token_secret = 'HJWYLX0NE3bdZc2Llyo0CBpc9bHT03mgyiMoSAn70'
consumer_key = 'QSzL0ZJstcIUtEvVv1UgyA'
consumer_secret = 'ljGWKSgxY807frB5uInEmJ506OzI1MZ4eOeoxKZw7g'
'''
# Michael:
'''
access_token = '986760717876506626-Hr2lP61w1Bd51SIdj4s4cB2354Bewxn'
access_token_secret = 'tU8uYYrRktgMQuP5eSfX2JFAPkBWcx4bcV0qF5SxlZARw'
consumer_key = "lPAnK5vlWiwlndUfinNcgEx03"
consumer_secret = "sTFwfqbDIxvG4mdpXPDxqd8Jtc4BDiZPDFoOtE4us8V7iR3ckh"
'''
access_token = '986715202094813184-UPrbmoyyIK1eDo7H8XEWZcUCsV99JOq'
access_token_secret = 'ni1bBzExCwxoml1Ur8G8KjTlsh9EuMZ99ZfFhcuan51td'
consumer_key = "rHyaOmsKI60MRVHrwtg37MQ99"
consumer_secret = "9dmshplZCCJ6jxbF99VvTCh2lW9O0Vx3njSj8t1zvNdpBd1fI1"

api = twitter.Api(consumer_key,
                  consumer_secret,
                  access_token,
                  access_token_secret)

results = api.GetStreamFilter(track=["Donald Trump", "India","F-1", "H1B", "H1-B", "Immigration" ])

for tweet in results:
    try:
        #tweet_jsonObject = json.loads(tweet)
        transformed_tweet = transform_tweet(tweet)
        index_to_solr(transformed_tweet)
    except Exception as e:
        print(e)
        traceback.print_exc
        sys.exit()
