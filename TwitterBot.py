from twitter_scraper import get_tweets
import markovify
import twitter

# Twitter API settings
# These are in our Discord server!
# DO NOT COMMIT TO GIT WITH THE API KEYS



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
user = "InternetofShit"
count = 5

tweets = scrape(user, count)
print(tweets.split('\n')[100])
textModel = generate(tweets)
printShortModel(textModel, 140)
#status = api.PostUpdate(Message Content)
