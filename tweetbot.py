import tweepy
import time

# START OF USER VARIABLES
consumer_key = "FILL"
consumer_secret = "FILL"
access_token = "FILL"
access_token_secret = "FILL"
keywords = [""]

#END OF USER VARIABLES

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
statuses = api.user_timeline(id =735983280609230848, count = 100)

def delete_status():
    statuses = api.user_timeline(id =4866870394, count = 100)
    for status in statuses:
        api.destroy_status(status.id_str)
    print("Tweets deleted.")

def concours_no_follow():
	for tweet in tweepy.Cursor(api.search,q="concours").items(1000):
		if "gagner" in tweet.text.lower() or "remporter" in tweet.text.lower():
			if "retweet" in tweet.text.lower() or "RT" in tweet.text:
				if "follow" not in tweet.text.lower():
					try:
						api.retweet(tweet.id)
					except tweepy.TweepError as e:
						print(e.reason)

def concours_follow():
	for tweet in tweepy.Cursor(api.search,q="concours").items(150):
#		if "retweet" in tweet.text.lower() or "rt" in tweet.text.lower():
#			api.retweet(tweet.id)
			if "follow" in tweet.text.lower():
				api.create_friendship(user_id =tweet.user.id)
				api.retweet(tweet.id)


choix = 0
print("1. Delete all tweets from account")
print("2. Participate to contests without following")
choix = int(input("Your choice : "))
if choix == 1:
	delete_status()
elif choix == 2:
	concours_no_follow()
