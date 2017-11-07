from __future__ import unicode_literals
import sys
import requests
import http.client # module for making HTTP request to website
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import time
import json
import billboard
import webbrowser
import urllib
import urllib.request
from requests import get
import youtube_dl
import json
import billboard
import pafy

import timeit
start_time = timeit.default_timer()

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
api="https://content.googleapis.com/youtube/v3/search?q="
api3="&maxResults=25&part=snippet&key=$$$YOUTUBE_API_KEY$$$"

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def file():
	lines = [line.rstrip('\n') for line in open('list.txt')]
	for test in lines:
		print("Downloading {0}".format(test))
		search=(test).replace(' ','%20')
		url=api+search+api3
		r = requests.get(url)
		cont = (r.json())
		videoid=cont['items'][0]['id']['videoId']
		print("Video found:Parsing json")
		nn='https://www.youtube.com/watch?v='+videoid
		try:
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download([nn])
		except:
			print("Convert Error")
		print("Video Downloaded\n\n")
n=0
while n<10:

	print("1)Enter \"bill\" for checking billboard top 100\n2)Enter \"exit\" to exit\n4)Enter file to read file mp3's")
	test=input("3)Enter song name:")
	if(test=="bill"):
		chart = billboard.ChartData('hot-100')
		print(chart)
		break
		exit
		n=10
	if(test=="exit"):
		n=10
		break
	if(test=="file"):
		file()
		n=10
		break
	else:
		search=(test).replace(' ','%20')
		#print(search)
		url=api+search+api3
		#print(url)
		r = requests.get(url)
		#print(r)
		#try:
		#uprint(r.json())
		cont = (r.json())
		videoid=cont['items'][0]['id']['videoId']
		#uprint(cont['items'][0]['id']['videoId'])
		#videoid=(r.json())
		print("Video found:Parsing json")
		nn='https://www.youtube.com/watch?v='+videoid
		"""video = pafy.new(nn)
		audiostreams = video.audiostreams
		audiostreams[1].download()"""
		try:
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download([nn])
		except:
			print("Convert Error")
		print("Video Downloaded\n\n")

elapsed = timeit.default_timer() - start_time
print(elapsed)
