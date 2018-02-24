from twitter_scraper import get_tweets
import markovify
import twitter

# Twitter API settings
# These are in our Discord server! 
# DO NOT COMMIT TO GIT WITH THE API KEYS

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

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

if __name__ == '__main__' :
	from sys import argv
	myargs = getopts(argv)
	if '-u' in myargs :  # Example usage.
		user = myargs['-u']
	if '-c' in myargs :
		count = int(myargs['-c'])

#tweets = scrape(user, count)
#print(tweets.split('\n')[100])
#textModel = generate(tweets)
#printShortModel(textModel, 140)
#status = api.PostUpdate(Message Content)