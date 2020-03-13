# twitterexaqmple.py
# Demonstrates connecting to the twitter API and accessing the twitter stream
# Author: Michael Fahy
# Email: fahy@chapman.edu
# Course: CPSC 353
# Assignment: PA01 Sentiment Analysis
# Version 1.2
# Date: February 15, 2016

# Demonstrates connecting to the twitter API and accessing the twitter stream

import twitter
import json
import sys
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

CONSUMER_KEY = 'Dt5uHM8LAXBxtNByoBtMERJ6l'
CONSUMER_SECRET = 'AjOgHoaJcWtq0FuXiQ68FEMaJKOwkdExIUBuwwiGCvcNS2yPnV'
OAUTH_TOKEN = '1236883534591045632-67PrgEtMBlbD0dWkriuy5JVRsaqPME'
OAUTH_TOKEN_SECRET = 'G8jahz894uQu21RJPEZmIbTTRFmT8FGVImgMBJ6eDdbeI'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

def sentiment(userInput):
    count = 1000
    search_results = twitter_api.search.tweets(q=userInput, count=count)
    statuses = search_results['statuses']

    status_texts = [status['text']
    for status in statuses]

    words = [w
             for t in status_texts
             for w in t.split()]

    score = 0
    for word in words:
        if word in scores.keys():
            score = score + scores[word]
    return score

sent_file = open('AFINN-111.txt')

scores = {}  # initialize an empty dictionary
for line in sent_file:
    term, score = line.split("\t")
    scores[term] = int(score)

word1 = input("Enter a search term for twitter:")

word2 = input("Enter a search term for twitter:")

score1 = sentiment(word1)
score2 = sentiment(word2)

if (score1 > score2):
    print (word1 + "Bigger sentiment value than" + word2)

elif (score2 < score1):
    print (word2 + "Bigger sentiment value than" + word1)
