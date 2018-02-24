from twitter_scraper import get_tweets
import markovify
#import python-twitter

#twitterAPI = twitter.Api(consumer_key='pc3BkUsw3fYRFowN4WTQOBphq',
#                  consumer_secret='	IqHm6E3nvK75RoxBTpz3Uu87cC4pL3aBrvqU7sot876CyRD7Te',
#                  access_token_key='967489509159038985-0P1B80wqyeOS6DBJPRmqQR1cFCIK0Zl',
#                  access_token_secret='Kfs3XNHwEPcdwsSOIntAKLLOHCnppfnh94pCtCYb4OIKm')

def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def scrape(account, numPage) :
	tweets = '\n'.join([t for t in get_tweets(account, pages=numPage)])
	return tweets

def generate(tweetData) :
	text_model = markovify.Text(tweetData)
	return text_model

def printShortModel(textModel, size) :
	print(textModel.make_short_sentence(size))

user = "InternetofShit"
count = 1

if __name__ == '__main__' :
	from sys import argv
	myargs = getopts(argv)
	if '-u' in myargs :  # Example usage.
		user = myargs['-u']
	if '-c' in myargs :
		count = int(myargs['-c'])

tweets = scrape(user, count)
print(tweets.split('\n')[3])
#textModel = generate(tweets)
#printShortModel(textModel, 140)
#print(twitterAPI.VerifyCredentials())