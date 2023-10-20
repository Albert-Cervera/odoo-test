import tweepy

def postTweet():
    twitter_auth_keys = {
        "consumer_key"        : "",
        "consumer_secret"     : "",
        "access_token"        : "",
        "access_token_secret" : ""
    }

    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)

    tweet = "Yet Another day, another #scifi #book and a cup of #coffee"
    post_result = api.update_status(status=tweet)

print("Trying to post ...")
postTweet();