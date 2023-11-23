
# this is a really ^simple^ program to download a palylist from a youtube ... 

import sys
from pytube import Playlist

def downloadPlaylist(playListURL, startingVid):
    # playListURL is the url for the playlist you want to download
    # startingVid is the number of the video you want t start from ( the first video is 1, the second is 2 etc... ) 
    playList = Playlist(playListURL)
    print(f'Downloading all videos in {playList.title} in highest resolution.')
    print("DO NOT PANIC IF IT LOOKS STUCK. EVERYTHING IS FINE jsut be patient :D")
    i = startingVid-1
    while i < len(playList.videos):
        try:
            print(f"downloading >> {playList.videos[i].title} ")
            playList.videos[i].streams.get_highest_resolution().download()
            print(f"{playList.videos[i].title} >> Downloaded. ")
        except:
            print(f"FAIL  >>>  {playList.videos[i].title }\nRetrying...(Press Ctrl + C to stop the script)")
            continue
        i = i+1
	print("The playlist has been downloaded !!")
    return 0 
#URL = sys.argv[1] # first argument after the script name >> uncomment this to use terminal arguments
#startingFrom = sys.argv[2] # the second argument after the script name >> uncomment this to use terminal arguments
URL = input("Enter the URL of the playlist >_ ")
startingFrom = int(input("Enter the starting video number ( writre 1 for the first video in the playlist)"))
#print(f"URL is {URL}") # testing.. 
#print(f"starting from is {startingFrom}") # testing..
downloadPlaylist(URL, startingFrom)