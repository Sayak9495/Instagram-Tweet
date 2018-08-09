# -*- coding: utf-8 -*-

"""Main module."""
import os
import tweepy
import oauth2 as oauth
import requests
import urllib2
from bs4 import BeautifulSoup
import re

def twitter_api():
	consumer_key = 'cklOCaJk5KI9pWTr45JqsSRV3'
	consumer_secret = 'p0pgEnkVRDkaPS9wZup75bNdnRdlOOfBMwIXf72dNSNrf8Jkz6'
	access_token = '1021066006792265729-iFXZqhEqa2z80SrIh7gSDRWcOS6u6z'
	access_token_secret = 'Lsf0wTKp35JKwPvnrctz1GJTRDr8knuArBcxhSUOodYZs'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	return api

def tweet_image(url, message):
    api = twitter_api()
    filename = 'temp.jpg'
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unable to download image")


def insta_tweet(page_name):
	page = "https://www.instagram.com/"+page_name+"/"
	page = urllib2.urlopen(page)
	soup = BeautifulSoup(page, "html.parser")
	script = soup.findAll('script')[3].string
	ind=script.find('= {')
	script=script[ind+1:]

	f= open("../page_names/"+page_name+".txt","r")
	check = f.read()


	indxs = [m.start() for m in re.finditer('display_url', script)]
	caption_indx = [m.start() for m in re.finditer('"text":"', script)]

	jpgs = [m.start() for m in re.finditer('.jpg",', script)]
	flag,cap_indx=0,0
	for indx in indxs:
		for i,jpg in enumerate(jpgs):
			if jpg>indx:
				url = script[indx+14:jpg+4]
				jpgs=jpgs[i:]
				break
		if url.split("/")[-1]==check:
			break
		else:
			if caption_indx[cap_indx]<indx:
				
				start=caption_indx[cap_indx]
				close=script[start:start+1500].find('"}')
				caption = script[start+8:start+close]
				if len(caption)>215:
					caption=caption[:215]
				cap_indx+=1
			else:
				caption=""
			if flag==0:
				f= open("../page_names/"+page_name+".txt","w")
				f.write(url.split("/")[-1])
				flag=1
				
			msg=caption + " Credit - https://www.instagram.com/"+page_name
			#print(url)
			#tweet_image(url,msg)
	return "DONE"
	f.close()


page_name=["programmer.me","godemperormusk","alpha_leaders","webprogramlife"]
for names in page_name:
	insta_tweet(names)