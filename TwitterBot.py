from twitter_scraper import get_tweets
import markovify
import twitter
from twitter import *
import random
import time

# Twitter API settings
# These are in our Discord server!
# DO NOT COMMIT TO GIT WITH THE API KEYS

api = twitter.Api(consumer_key='fZpJFlF9Fe8z1adti8V0j0Zlt',
                  consumer_secret='L2kqzY5WWcGZTuHYahr22ovFLAuGehOosjAuhumzjBrK59r87B',
                  access_token_key='967489509159038985-47bTD4KSnlDo1xHVR2NgKwUNrThJhDG',
                  access_token_secret='0wqifsXDexMA5IScnlKQ23a4lTI6kXrJN9NCMo6NW2q4a')

# Methods for scaping and for markov generation
def scrape(account, numPage) :
	tweets = '\n'.join([t for t in get_tweets(account, pages=numPage)])
	return tweets

def generate(tweetData) :
	text_model = markovify.Text(tweetData)
	return text_model

def printShortModel(textModel, size) :
	print(textModel.make_short_sentence(size))

# Default values for opts
# user = "Lord_Voldemort7" CHOICE 1
user = "Lord_Voldemort7"
count = 20

def MarkovVsReal(tweets, texModel) :
	real = random.choice(tweets.split('\n'))
	mark = textModel.make_short_sentence(100)
	out = "Which is the real one? DM me with 'q1' and your answer (a or b)\nA. " + real + '\nB. ' + mark
	print(out)
	print("\n\n%d" % len(out))

correct = []

def checkDM() :
	dms = api.GetDirectMessages()
	for dm in dms :
		if 'Q1' in dm.text or 'q1' in dm.text and dm.sender_id not in correct :
			if 'a' in dm.text or 'A' in dm.text :
				correct.append(dm.sender_id)
				api.PostDirectMessage("Congratulations! Continue on Discord https://discord.gg/u9mrDVe", dm.sender_id)
				api.DestroyDirectMessage(dm.id)
			if 'b' in dm.text or 'B' in dm.text :
				api.PostDirectMessage("Sorry! That is incorrect. Please try again", dm.sender_id)

def destroySent() :
	sent = api.GetSentDirectMessages()
	for dm in sent :
		api.DestroyDirectMessage(dm.id)

def destroyReceived() :
	dms = api.GetDirectMessages()
	for dm in dms :
		api.DestroyDirectMessage(dm.id)

tweets = scrape(user, count)
textModel = generate(tweets)
MarkovVsReal(tweets, textModel)

while True :
	checkDM()
	destroySent()
	destroyReceived()
	time.sleep(60)
#status = api.PostUpdate(Message Content)
