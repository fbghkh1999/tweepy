import tweepy
import pandas as pd

consumer_key = 'WtRSaMB6kYT72y46xaYEh06vL'
consumer_secret = 'RPUPWKQ8sBIhdr2MNDKUYXkJoLGHJ5ucbhVfkO52EzhfBcvtdS'
access_token = '951514823350784001-TWnMDlRKBS52h84u2ZrvtQWu6XKzIPh'
access_token_secret = 'S9bCQ8MRxZxs0zEIh207RkmxYns843kV0s5aCqAgH0pho'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_related_tweets(key_word):
    twitter_users = []
    tweet_time = []
    tweet_string = [] 
    for tweet in tweepy.Cursor(api.search,q=key_word, count=200).items(1000):
            if (not tweet.retweeted) and ('RT @' not in tweet.text):
                if tweet.lang == "en":
                    twitter_users.append(tweet.user.name)
                    tweet_time.append(tweet.created_at)
                    tweet_string.append(tweet.text)
                    print([tweet.user.name,tweet.created_at,tweet.text])
    '''df = pd.DataFrame({'name':twitter_users, 'time': tweet_time, 'tweet': tweet_string})
    df.to_csv(f"{key_word}.csv")
    return df'''
#df_joker =
get_related_tweets("Joker")
#print(df_joker.head(5))