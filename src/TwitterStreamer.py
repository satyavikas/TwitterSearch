from twitter import *
from tweet_transformer import transform_tweet
import json
from solr_indexer import index_to_solr
import sys
import traceback

access_token = '636984272-kV5vKBpz9QJ46UZP8yVmXSulLqLYh55suNinHzmM'
access_token_secret = 'HJWYLX0NE3bdZc2Llyo0CBpc9bHT03mgyiMoSAn70'
consumer_key = 'QSzL0ZJstcIUtEvVv1UgyA'
consumer_secret = 'ljGWKSgxY807frB5uInEmJ506OzI1MZ4eOeoxKZw7g'

t = Twitter(
    auth=OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

tweet_stream = t.search.tweets(q="Donald Trump").statuses()

for tweet in tweet_stream:
    print(tweet)
    try:
        #tweet_jsonObject = json.loads(tweet)
        transformed_tweet = transform_tweet(tweet)
        index_to_solr(transformed_tweet)
    except Exception as e:
        print(e)
        traceback.print_exc
        sys.exit()
