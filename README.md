# Twitter Crawler
### Rashid Goshtasbi and Brendan Cheng
SID: 861056442 and 861055750

Hello there! T-Crawler is an open source project for Linux to download tweets over twitter that has geolocation enabled.

## Collaboration Details
Description of contribtutions of each team member
### Rashid Goshtasbi
* Figuring out an API to use
* Researching instructions to download additional libraries to incorporate with API and product feature
* Researching on implimentation on API
* Creating Twiter account and signing up for Twitter Developer Access for special keys required by API
* Figuring our nesseccary functions to use to run library functions
* **Coding**: Configurign twitter API streaming functions:

		l = listener()
		auth = OAuthHandler(ckey, csecret)
		auth.set_access_token(atoken, asecret)
		
		while True:
			try:
			twitterStream = Stream(auth, l)
			twitterStream.filter(locations=[-180,-90,180,90], languages=["en"])
		except:
			continue

* **Coding**: Contributing to converting streaming tweets to JSON format to parse:

		with open("tweets"+str(numFile)+".txt", 'a') as output:
				if(os.path.getsize("tweets"+str(numFile)+".txt") < 10000000):					
					#LOADS ALL OF THE TWEET DATA INTO VARIABLE "TWEET"
					tweet = json.loads(data)
* **Coding**: Contributed to parsing tweets for url links:

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

* **Coding**: Contributed to retrieving title of url link in tweet's text
* Implementing of "**try:**" and "**except:**" protocols:

		...
		try:
		...
		except:
		...
*  Figuring out how to output each JSON string onto a NEWLINE in our output file
*  Figured out how to output each file into any computer using:

		#path for files to save
		path = os.getcwd()

### Brendan Cheng
* Researching instructions to download additional libraries to incorporate with API and product feature
* Researching on implimentation on API
* **Coding**: Configurign twitter API streaming functions:

		l = listener()
		auth = OAuthHandler(ckey, csecret)
		auth.set_access_token(atoken, asecret)
		
		while True:
			try:
			twitterStream = Stream(auth, l)
			twitterStream.filter(locations=[-180,-90,180,90], languages=["en"])
		except:
			continue

* **Coding**: Contributing to converting streaming tweets to JSON format to parse:

		with open("tweets"+str(numFile)+".txt", 'a') as output:
				if(os.path.getsize("tweets"+str(numFile)+".txt") < 10000000):					
					#LOADS ALL OF THE TWEET DATA INTO VARIABLE "TWEET"
					tweet = json.loads(data)
* **Coding**: Contributed to parsing tweets for url links:

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

* **Coding**: Contributed to retrieving title of url link in tweet's text
* Report on limitations, data structures
* Figuring out how to output each JSON string onto a NEWLINE in our output file

## Overview of System

## Limitations
* Need to install additional libraries to use program

## Instructions
##### May vary depending on Operating System, examples below were used on Linux OSX
NOTE: Program will download files to the current directory you have cloned the github to or where you have the file in

1. Instll PIP: In terminal, type in: **sudo easy_install pip**
2. Install tweepy API: In terminal, type: **sudo pip install tweepy**
3. Install BeautifulSoup: In terminal, type in: **sudo pip install beautifulsoup4**
4. clone program from **https://github.com/rgosh001/tweets.git** or copy tcrawler.py program to a directory of your choice
5. 
