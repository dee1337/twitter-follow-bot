#-------------------------------------
# code could be more efficient, but as a newbie in python,
# i just want something that works ;-)
# - no twitter api required (= no calling limits) - 
# - use twitterParser_oldProfile(twittername) for OLD Twitter Design only
# - use twitterParser_oldProfile(twittername) for NEW Twitter Design only
# (basically, if you see an error, switch to the other function)
#--------------------------------------
from bs4 import BeautifulSoup
import requests

# faking header, twitter should not know that we connect with python 
# - just for the (worst) case...
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36'}

def twitterParser_oldProfile(nickname):
	""" takes a twitter nickname and returns a list with:
	[tweets, following, followers] 
	ONLY WORKS FOR OLD TWITTER PROFILE DESIGNS! [before april 2014]
	"""
	stats = []
	try:
		url = "http://twitter.com/"+nickname
	except Exception(e):
		print e
	print "retrieving url:", url
	url = requests.get(url, headers=header)
	webpage = BeautifulSoup(url.text)
	result = webpage.find_all("strong","js-mini-profile-stat")
	result = str(result)
	i=0
	endpos = 0
	while i < 3:
		startpos = result.index('title="', endpos)
		endpos = result.index('">', startpos)
		stats.append(result[startpos+len('title="'):endpos])
		i += 1
	return stats

def twitterParser(nickname):
	""" takes a twitter nickname and returns a list with:
	[tweets, following, followers] 
	ONLY WORKS FOR NEW TWITTER PROFILE DESIGN (~April 2014)
	""" 
	stats = []
	try:
		url = "http://twitter.com/"+nickname
	except Exception(e):
		print e
	print "retrieving url:", url
	url = requests.get(url, headers=header)
	webpage = BeautifulSoup(url.text)
	tweets = webpage.findAll("a","ProfileNav-stat")[0].getText()
	following = webpage.findAll("a","ProfileNav-stat")[1].getText()
	followers = webpage.findAll("a","ProfileNav-stat")[2].getText()
	#print [tweets, following, followers]
	tweets = [tweets, following, followers]
	tweet2 = []
	i= 0
	while i < len(tweets):
		tweet2.append(tweets[i].split('\n'))
		i += 1
	tweet2[0][2] = str(tweet2[0][2]).lstrip()
	tweet2[1][2] = str(tweet2[1][2]).lstrip()
	tweet2[2][2] = str(tweet2[2][2]).lstrip()
	result = [tweet2[0][2], tweet2[1][2], tweet2[2][2]]
	return result
