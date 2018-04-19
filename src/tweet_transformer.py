from datetime import datetime
import time
from textblob import TextBlob


def transform_tweet(tweet_jsonObject): #method to cover your jsonobject tweet into required transformation.
    transformed_tweet = {} #creating an empty dictionary to store tweet of required
    
    transformed_tweet['id'] = tweet_jsonObject['id'] 
    
    transformed_tweet['plaintext'] = tweet_jsonObject['text'] 
    
    transformed_tweet['hashtags'] = tweet_jsonObject['entities']['hashtags'] if tweet_jsonObject['entities']['hashtags'] is not None else ['None'] 
    
    transformed_tweet['created_at'] = format_date(tweet_jsonObject['created_at']) 
    
    transformed_tweet['screen_name'] = tweet_jsonObject['user']['screen_name']
    
    transformed_tweet['lang'] = tweet_jsonObject['user']['lang']
    
    transformed_tweet['latlong'] = get_coordinates(tweet_jsonObject['coordinates'])
    
    # Sentimental Analysis
    tweet_text = tweet_jsonObject['text'] 
    
    nouns = list ( TextBlob(tweet_text).noun_phrases ) 
    polarity = TextBlob(tweet_text).sentiment.polarity 
    subjectivity = TextBlob(tweet_text).sentiment.subjectivity  
    
        
    transformed_tweet['nouns'] = nouns 
    transformed_tweet['polarity'] = float("{0:.2f}".format(polarity))#finding the sentimental analysis of emotions from given scale
    transformed_tweet['subjectivity'] = float("{0:.2f}".format(subjectivity)) # finding subjectivity of the text whether its a  opinion or fact
    
    # TODO: Remind to do ReactionRNN Sentimental analysis later. 
    
    return transformed_tweet
    
    
    
def format_date(twitter_date): #method to format the date
    # sample = 'created_at': 'Mon Feb 19 20:01:21 +0000 2018'
    
    solr_dateformat = '%Y-%m-%dT%H:%M:%SZ'  # given two formats of the date
    twitter_format = '%a %b %d %H:%M:%S +0000 %Y'
    
    twitter_date_obj  = datetime.strptime(twitter_date, twitter_format) 
    formatted = datetime.strftime(twitter_date_obj,solr_dateformat) # 
    
    return formatted

def get_coordinates(twitter_coordinates): # method to get (lat long ) geospatial location
    
    if twitter_coordinates is not None: # if given coordinates in data
        lat = str(twitter_coordinates['coordinates'][0]) #to fetch the lat value from coordinates
        long = str(twitter_coordinates['coordinates'][1])#to fetch the long value from coordinates
        
        return lat + ',' + long # joining or concatinating both  lat and long
    else:
        return '0.00,0.00' #result in solr coordinate format
    
        
    
    
    
    pass

if __name__ == '__main__':
    
    #sample_twitter_date = 'Mon Feb 19 20:01:21 +0000 2018'
    
    #format_date(sample_twitter_date)
    '''
    sample_coordinates_obj = {"coordinates":
                              {
                                  "coordinates":
                                  [
                                      -75.14310264,
                                      40.05701649
                                      ],
                                  "type":"Point"
                                  }
                              }
    print(get_coordinates(sample_coordinates_obj['coordinates']))
    '''
    #YYYY-MM-DD
    
    my_date = "2017-02-19"
    
    # DD-MM-YYYY
    
    date_obj = datetime.strptime('%Y-%m-%d', my_date)
    
    wanted_format = datetime.strftime(date_obj, '%d-%m-%Y')
    
    print(wanted_format)
    
    
    
    
    
    