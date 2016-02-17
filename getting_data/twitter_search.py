from twython import Twython
import json

credential_file = open("credentials.json", "r")
credentials = json.load(credential_file)
credential_file.close()
CONSUMER_KEY = credentials["consumer_key"]
CONSUMER_SECRET = credentials["consumer_secret"]
twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

# search for tweets containing the phrase "data science"
for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"].encode('utf-8')
    text = status["text"].encode('utf-8')
    print user, ":", text
    print 