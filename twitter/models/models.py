# -*- coding: utf-8 -*-
import tweepy
from odoo import models, fields, api


class twitter(models.Model):

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


    _name = 'twitter.twitter'
    _description = 'twitter.twitter'

    tweet = fields.Text();

    """
     Post new tweet
    """
    post_result = api.update_status(status=tweet)
