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
import logging


def extractor(worker_id):

    # TreyPitaKoum
    access_token = '986715202094813184-UPrbmoyyIK1eDo7H8XEWZcUCsV99JOq'
    access_token_secret = 'ni1bBzExCwxoml1Ur8G8KjTlsh9EuMZ99ZfFhcuan51td'
    consumer_key = "rHyaOmsKI60MRVHrwtg37MQ99"
    consumer_secret = "9dmshplZCCJ6jxbF99VvTCh2lW9O0Vx3njSj8t1zvNdpBd1fI1"

    # Logging Settings
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler('/var/log/TwitterSearch/TwitterBear_TPK_worker_{0}.log'.format(worker_id))
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    api = twitter.Api(consumer_key, consumer_secret, access_token, access_token_secret)

    results = api.GetStreamFilter(track=["Donald Trump", "India", "F-1", "H1B", "H1-B", "Immigration", "OPT", "Green Card", "USCIS"])

    count = 0
    error_count = 0
    for tweet in results:
        count += 1
        try:
            transformed_tweet = transform_tweet(tweet)
            try:
                index_to_solr(transformed_tweet)
            except Exception as e:
                print(e)
                logger.error("Exeption: {0} | Error Count so far: {2}   |   Tweet: {1}".format(e, json.dumps(tweet), error_count))
                pass
        except Exception as e:
            error_count += 1
            print(e)
            traceback.print_exc
            logger.error("Exeption: {0} | Error Count so far: {2}   |   Tweet: {1}".format(e, json.dumps(tweet), error_count))
            pass
        if count % 1000 == 0:
            logger.info("Processed {0} so far. Error Count so far: {1}".format(count, error_count))


if __name__ == '__main__':
    # The worker_id for this Script.
    worker_id = str(sys.argv[1])
    extractor(worker_id)