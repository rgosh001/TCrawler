from HTMLParser import HTMLParser
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import os
import sys
import random
import requests
from bs4 import BeautifulSoup
import re
import urllib
import urllib2
#path for files to save
#path = "/Users/RashidGoshtasbi/tweets"
path = os.getcwd()

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
		global url_text
		global numFile
		global finalSize
		global tweet 
		#global text
		global text_tweet
		global str1
		global link_text
		try:
			with open("tweets"+str(numFile)+".txt", 'a') as output:
				if(os.path.getsize("tweets"+str(numFile)+".txt") < 10000000):
					# tweet[u'linktitle']=title
					
					#LOADS ALL OF THE TWEET DATA INTO VARIABLE "TWEET"
					tweet = json.loads(data)
					
					
					#THIS IS THE TEXT ONLY OF THE TWEET
					text_tweet = tweet[u'text']
					
					str1 = "http"
										
					#IF STATEMENTS LOOKS FOR TWEETS THAT HAVE TITLE
					#IF IT DOESNT HAVE A URL, IT DOESNT PARSE IT
					if (text_tweet.find('http') != -1):
						url_text = text_tweet.find(str1)
						link_text = text_tweet[url_text:url_text+23]
						#print link_text
						
						content = urllib2.urlopen(link_text).read()
						soup = BeautifulSoup(content, "html.parser")
						tweet[u'linktitle']= soup.title.string
					else:
						pass
						
					#text = json.loads(tweet)
					#WRITES ORIGINAL TEXT INTO FILE
					#print json.dumps(tweet)
					
#					json.dump(tweet + '\n',output)
					out = json.dumps(tweet)
					output.write(out + '\n')

#					output.write(tweet)
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

#	def on_error(self, status):
#		print status

if __name__ == '__main__':

	l = listener()
	auth = OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	
	while True:
		try:
			twitterStream = Stream(auth, l)
			twitterStream.filter(locations=[-180,-90,180,90], languages=["en"])
		except:
			continue

