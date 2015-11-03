from HTMLParser import HTMLParser
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import os
import sys
import random
from bs4 import BeautifulSoup
import re
import urllib
import urllib2
import bs4

#path for files to save
path = "/Users/RashidGoshtasbi/tweets"

#5GB required for downloads
finalSize = 500

#Number of file for multiple file creations
numFile = 1

#consumer key, consumer secret, access token, access secret.
ckey="ieLD5TpJV7ruiDgXlMZAFGrV2"
csecret="t3IFbnMdMnHx9oG0brfsLkuEh44nzsyRUsl3RsWPTyoGcYo2HB"
atoken="32316013-GPuYYrD0XtPL0GBJHGdAvCQKEwaOxYbF0I0E4Xrp7"
asecret="RP0tJAc9rYnQssJkT6EXfCActzLbxfLoiWcX62IbrE2n0"

class listener(StreamListener):
	def on_data(self, data):
		global numFile
		global finalSize
		try:
			with open("tweets"+str(numFile)+".txt", 'a') as output:
				if(os.path.getsize("tweets"+str(numFile)+".txt") < 10000000):
					# store this into anoother variable
					# parse and get the link
					# fetch the title of the webpage
					# tweet[u'linktitle']=title
					
					tweet = json.loads(data)
					text_tweet = tweet[u'text'] #THIS IS THE TEXT ONLY OF THE TWEET
					print text_tweet
										
#					#use tweet_text to get url and save it into variable and enter below
#					soup = BeautifulSoup(urllib2.urlopen(link_text))
#					link_title = soup.title.string
#					
#					#WRITES ORIGINAL TEXT INTO FILE
#					output.write(tweet)
#					output.write('\n')
#					output.close()
					
					return(True)
					
				else:
					if (numFile < finalSize):
						numFile += 1
					else:
						os._exit(0)
						
		except BaseException, e:
			print 'failed,', str(e)
			#time.sleep(1)

	def on_error(self, status):
		print status
		
if __name__ == '__main__':

	l = listener()
	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	twitterStream = Stream(auth, l)
	twitterStream.filter(locations=[-180,-90,180,90], languages=["en"])

