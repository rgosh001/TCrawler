from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import os

#path for files to save
path = "/Users/RashidGoshtasbi/twitter/tweets"

#5GB required for downloads
FinalSize = 500

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
		try:
			#print (data)
			
			timeStamp = data.split('created_at":"')[1].split('","id"')[0]
			#print timeStamp
			
			tweet = data.split(',"text":')[1].split(',"source')[0]
			#print tweet
						
			saveThis = timeStamp + '##' + tweet
			saveFile = open('data1.csv', 'a')
			saveFile.write(saveThis)
			saveFile.write('\n')
			saveFile.close()
			return(True)
		except BaseException, e:
			print 'failed,', str(e)
			time.sleep(1)

	def on_error(self, status):
		print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(locations=[-180,-90,180,90], languages=["en"])