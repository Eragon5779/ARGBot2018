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
scrapeUsers = ["Lord_Voldemort7", "metaprophet", "InternetofShit", "deathstarpr", "dennysdiner", "automatofstyle"]#, "firstworldpains", "lmao"]
count = 20
answer = ""
def MarkovVsReal(tweets, texModel) :
	real1 = ""
	while not real1 or real1 == "" or ".com" in real1 or "@" in real1 or "#" in real1 and len(real1) > 70:
		real1 = random.choice(tweets.split('\n'))
	real2 = ""
	while not real2 or real2 == "" or ".com" in real2 or "@" in real2 or "#" in real2 and len(real2) > 70:
		real2 = random.choice(tweets.split('\n'))
	mark = "@"
	while mark == "" or ".com" in mark or "@" in mark or "#" in mark :
		mark = textModel.make_short_sentence(70)
	
	global answer
	rnd = [0, 0, 1]
	shuffled = []
	random.shuffle(rnd)
	print(rnd)
	if rnd[0] == 1 :
		answer = 'a'
		shuffled.append(mark)
		shuffled.append(real1)
		shuffled.append(real2)
	elif rnd[1] == 1 :
		answer = 'b'
		shuffled.append(real1)
		shuffled.append(mark)
		shuffled.append(real2)
	else :
		answer = 'c'
		shuffled.append(real2)
		shuffled.append(real1)
		shuffled.append(mark)

	out = "Which is the fake tweet? DM me with 'q1' and your answer (a, b, c)\nA. " + shuffled[0] + '\nB. ' + shuffled[1] + '\nC. ' + shuffled[2]
	print(out)
	print("\n\n%d" % len(out))

correct = []

def checkDM() :
	dms = api.GetDirectMessages()
	for dm in dms :
		if ('Q1' in dm.text or 'q1' in dm.text) and dm.sender_id not in correct :
			if answer in dm.text.lower() :
				correct.append(dm.sender_id)
				api.PostDirectMessage("Congratulations! Continue on Discord https://discord.gg/u9mrDVe", dm.sender_id)
				api.DestroyDirectMessage(dm.id)
			else :
				api.PostDirectMessage("Sorry! That is incorrect. Please try again", dm.sender_id)
				api.DestroyDirectMessage(dm.id)

def destroySent() :
	sent = api.GetSentDirectMessages()
	for dm in sent :
		api.DestroyDirectMessage(dm.id)

tweets = ""

for user in scrapeUsers :
	tweets += scrape(user, count) + "\n"

print(len(tweets))

textModel = generate(tweets)
MarkovVsReal(tweets, textModel)

while True :
	checkDM()
	destroySent()
	time.sleep(60)
#status = api.PostUpdate(Message Content)
