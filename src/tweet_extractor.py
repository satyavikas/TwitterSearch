'''
Created on Feb 19, 2018

@author: Satya
'''
import json
from pprint import pprint
import sys

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

from solr_indexer import index_to_solr
from tweet_transformer import transform_tweet


#Variables that contains the user credentials to access Twitter API
#old
'''
access_token = '872220241-8CZ3qp1ThhMgGUrB7Ze04zrKSfp4zMDW2Xyi5GUH'
access_token_secret = 'JQiBVbem3VnqT2GnPL1Hp8FFPz2u3iBnCNRL4T3YDubJW'
consumer_key = "m83GLOfNY2fZxqBIOI9byoTRi"
consumer_secret = "ZTN2JdLewEWq6SWVxNvRrpqcv5nXb0U0pByEGKvKas7thML5zO"
'''
#new 
'''
access_token = '986715202094813184-UPrbmoyyIK1eDo7H8XEWZcUCsV99JOq'
access_token_secret = 'ni1bBzExCwxoml1Ur8G8KjTlsh9EuMZ99ZfFhcuan51td'
consumer_key = "rHyaOmsKI60MRVHrwtg37MQ99"
consumer_secret = "9dmshplZCCJ6jxbF99VvTCh2lW9O0Vx3njSj8t1zvNdpBd1fI1"
'''
'''
# third
access_token = '872220241-3WShh8Uq2BpdD4u0WqD69euInwZ3m6k41GwWyEVU'
access_token_secret = 'I4T1M2FicgXKMvuz2RWfmTpXCxJEWW5c4TB0n3cfx6bm8'
consumer_key = "Na3xYuW8FGmobN2G578v1mFyA"
consumer_secret = "OHLSuX2fiFLbjkYOKLhddZbmYNsuM5g8OCSWUcCEm1CKoU0vu6"
'''


# michael
access_token = '986760717876506626-Hr2lP61w1Bd51SIdj4s4cB2354Bewxn'
access_token_secret = 'tU8uYYrRktgMQuP5eSfX2JFAPkBWcx4bcV0qF5SxlZARw'
consumer_key = "lPAnK5vlWiwlndUfinNcgEx03"
consumer_secret = "sTFwfqbDIxvG4mdpXPDxqd8Jtc4BDiZPDFoOtE4us8V7iR3ckh"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):


    def on_data(self, data):
        
        tweet_count = 0 #1 intializing tweet count

        # 1: Convert tweet to JSON
        tweet_jsonObject = json.loads(data) 
        
        
        # 2: Transform the tweet to the wanted format
        transformed_tweet = transform_tweet(tweet_jsonObject)
        #print(transformed_tweet)
        tweet_count += 1   
        
        if tweet_count % 1000 == 0:
            print('---------------------- Number of tweets indexed so far: {0} -------------------------------'.format(tweet_count)) 
        
        # 3: Send the transformed to be indexed into Solr.
        index_to_solr(transformed_tweet)
        
        return True

    def on_error(self, status):
        print("Error Streaming tweets. Status: {0}".format(status))


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth,l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    while True:
        try:
            stream.filter(track=['nickolus Cruz', 'Gun Control', 'Donald Trump', 'Florida Shooting'])
        except:
            continue
        
