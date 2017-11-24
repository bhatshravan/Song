import pafy
import _thread
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import urllib.request
from requests import get

#Initializing all url
api="https://content.googleapis.com/youtube/v3/search?q="
api3="&maxResults=25&part=snippet&key=AIzaSyAjtQHN9pkXswmmvWLOfpzhEwA3uhUTiJM"

def print_time( test, i,imax):
	search=(test).replace(' ','%20')
	url=api+search+api3
	r = requests.get(url)
	cont = (r.json())
	videoid=cont['items'][0]['id']['videoId']
	print("Video found:Parsing json")
	nn='https://www.youtube.com/watch?v='+videoid
	video = pafy.new(nn)
	print(video.title)	
	print(video.viewcount, video.author)
	print(video.duration, video.likes, video.dislikes)
	streams = video.streams
	for s in streams:
		print(s.resolution, s.extension, s.get_filesize())
	ca=int(input("Enter which resolution from 0 to n to download or -1 to exit:"))
	if(ca==-1):
		print("EXIT")
	else:
		try:
			streams[ca].download()(quiet=False)
		except:
			print("Download succesfully completed, exiting the program")
	print("Video Downloaded\n\n")

	
#Taking input
print("\n\nEnter exit to exit\nEnter 'y' youtube search video direct download\nEnter 'u' for direct url")
test=input("\nEnter input:")

if test=="y":
	test=input("Enter video name:")
	_thread.start_new_thread( print_time, (test, 1,10 ) )

if test=="u":
	url=input("Enter url:")
	video = pafy.new(url)
	print(video.title)	
	print(video.viewcount, video.author)
	print(video.duration, video.likes, video.dislikes)
	streams = video.streams
	for s in streams:
		print(s.resolution, s.extension, s.get_filesize())
	ca=int(input("Enter case or -1 to exit:"))
	if(ca==-1):
		print("EXIT")
	else:
		try:
			streams[ca].download()(quiet=False)
		except:
			print("Download succesfully completed, exiting the program")
else:
	print("EXITING")
