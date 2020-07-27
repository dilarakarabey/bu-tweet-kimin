# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 2020

@author: Dilara Karabey

Install nest_asyncio to avoid "RuntimeError: This event loop is already running"
Run the script DIRECTLY under the Twint file to get rid of the AttributeError, if you get one.
"""

import twint
import nest_asyncio
nest_asyncio.apply()

def get_tweet(username):
    #Gets tweets by username since the specified date

    c = twint.Config()
    c.Lang = "tr"
    c.Username = username
    c.Since = "2019-04-01" #get tweets since the most recent election
    c.Store_csv = True #store in .csv format
    c.Custom["tweet"] = ["id", "created_at", "username", "tweet", "mentions", "likes_count", "retweet", "hashtags"]
    c.Output = username + ".csv"
	
    twint.run.Search(c)
    
get_tweet("RTErdogan")
get_tweet("kilicdarogluk")