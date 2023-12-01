
# this is a really ^simple^ program to download a palylist from a youtube ... 

# import sys # this is for future uses @TODO Implement system paramaters 
from pytube import Playlist, YouTube

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

def downloadSingleVideo(url):
    video = YouTube(url)
    try:
            print(f"downloading >> {video.title} ")
            video.streams.get_highest_resolution().download()
            print(f"{video.title} >> Downloaded. ")
    except:
        print(f"FAIL  >>>  {video.title }")
        return 0

def main():
    options = [
         "A)Adjsut the settings", "B)Download a playlist",
         "C)Download a single video", "D)Download a sequance of videos",
         "E)Download a single song", "F)Download a sequance of songs",
         "0)Exit"
    ]
    print('----| Welcome |----')
    print('What Do You Want To Do ? (Enter the letter)')
    for i in range(0, len(options)): 
         print(options[i])

    while True :
        character = input(">_ ")
        inputOption = (ord(character[0].upper()) - ord('A')) + 1 # this should give us the number of the selected option
        if inputOption < 1 or inputOption > 26: # that means no letter was entered so break the loop
            break
        if inputOption == 1:
            # Adjsut the settings
            continue
        elif inputOption == 2:
            # Download a playlist 
            playlsitUrl = input("Enter the URL of the Playlist. >_ ")
            playlistStartAt = input("Enter the starting video number ( writre 1 to start from the first video in the playlist) >_ ")
            if not playlistStartAt.isdecimal:
                playlistStartAt = 1
            else:
                playlistStartAt = int(playlistStartAt)
            downloadPlaylist(playlsitUrl, playlistStartAt)
        elif inputOption == 3:
            # Download a single video
            vidUrl = input("Enter the Video URL >_ ")
            downloadSingleVideo(vidUrl)
        elif inputOption == 4:
            # Download a sequance of videos
            print("Enter the all links you want to download and when you are done write done. ")
            links = []
            tmpLink = ''
            while True:
                tmpLink = input(">_ ")
                if tmpLink.lower() == "done":
                    break
                links.append(tmpLink)
            for url in links:
                downloadSingleVideo(url)
            
        elif inputOption == 5:
            # Download a single song 
            continue
        elif inputOption == 2:
            # Download a sequance of songs
            continue
        # elif inputOption == 2:
        #     # Option describtion 
        print("Done\nWhat's next ?")
        for i in range(0, len(options)): 
         print(options[i])
    print("Cya :d")
    return 0

if __name__ == "__main__":
         main()
