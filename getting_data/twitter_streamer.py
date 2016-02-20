from twython import TwythonStreamer
import json
from collections import Counter

tweets = []

class MyStreamer(TwythonStreamer):
    """this subclass of TwythonStreamer specifies how to interact with the 
    stream"""
    
    def on_success(self, data):
        """what do we do when twitter sends us data?
        here data will be a Python dict representing a tweet"""
        
        # only want to collect English-language tweets
        if data['lang'] == 'en':
            tweets.append(data)
            print "received tweet #", len(tweets)
        
        # stop when we've collected enough
        if len(tweets) >= 20:
            self.disconnect()
    
    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()
        
credential_file = open("credentials.json", "r")
credentials = json.load(credential_file)
credential_file.close()
CONSUMER_KEY = credentials["consumer_key"]
CONSUMER_SECRET = credentials["consumer_secret"]
ACCESS_TOKEN = credentials["access_token"]
ACCESS_TOKEN_SECRET = credentials["access_token_secret"]
stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# starts consuming public statuses that contain the keyword 'data'
stream.statuses.filter(track='Deadpool')

# if instead we wanted to start consuming a smaple of *all* public statuses
# stream.status.sample())

# most common hashtags
top_hashtags = Counter(hashtag['text'].lower()
                       for tweet in tweets
                       for hashtag in tweet["entities"]["hashtags"])
print top_hashtags.most_common(5)