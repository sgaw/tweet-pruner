import json
import collections

# TODO(make a main somewhere)

# Open test file with Tweet home stream response, ommitting HTTP header.
home_stream_str = ''
f = open('test-stream.json', 'r')
for line in f:
    home_stream_str += line
    
# JSON <-> Python list, dictionary
home_stream = json.loads(home_stream_str)
user_tweets = collections.defaultdict(list)
user_profiles = collections.defaultdict(dict)
for tweet_dict in home_stream:
    user_id = tweet_dict['user']['id']
    followers = tweet_dict['user']['followers_count']
    tweet_text = tweet_dict['text']
    retweet_count = tweet_dict['retweet_count']
    user_tweets[user_id].append((retweet_count, tweet_text))
    user_profiles[user_id] = tweet_dict['user']

for user_id, profile in user_profiles.iteritems():
    print str(user_id) + ', ' + profile['name']
    for retweets, text in sorted(user_tweets[user_id], reverse=True):
        print '* ' + str(retweets) + ':\t' + text
 
