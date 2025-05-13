#YouTube Video/Playlist Downloader
# Menu Driven program
"""----------------------------------------------------------------------------------"""

# other info
width = 80

# Heading
print ("-"*width)
print (("YouTube Video/Playlist Downloader").center(width))
print ("-"*width)

# Options
print ("Please make a choice;")
print ("\t1. Video downloading")
print ("\t2. Playlist downloading")
print ("\t3. Exit")

print (("-"*(int (width * 0.9))).center(width))

# importing functions from modules
# from signal import raise_signal
from pytube import YouTube, Playlist
from datetime import timedelta

# Download path
path = "F:\YouTube Downloads"

def PathNamer(PathAddress):
    PA = ""
    for i in PathAddress:
        if i in ''':*?"'<>/\|''':
            # PA += "/"
            break

        else: PA += i
    
    return PA.strip()

'''----------------------------------------------------------------------------'''
# main program
while True:

    # input
    choice = int (input ("\nEnter your choice: "))
    print (("-"*(int (width * 0.8))).center(width))

    if choice == 1:
        # heading
        print (("YouTube Video Downloader").center(width))
        print (("-"*(int (width * 0.8))).center(width))

        # main program
        while True:
            # ask for the link from user
            link = input("Enter YouTube Video URL:  ")

            if link == "": # Exit
                print ("Thank You for using Python YouTube Video Downloader!")
                break

            yt = YouTube(link)

            # Showing details
            print("\nTitle: ",yt.title)
            print("\nNumber of views: ",yt.views)
            print("Length of video: ",timedelta(seconds=yt.length))
            # print("Rating of video: ",yt.rating)
            # print ("\nDescription: ", yt.description)

            # Getting the highest resolution possible
            ys = yt.streams.get_highest_resolution()

            
            print("Downloading...")
            ys.download(path)
            print("Download completed!!\n")

    if choice == 2:

        # Heading
        print (("YouTube Playlist Downloader").center(width))
        print (("-"*(int (width * 0.8))).center(width))

        # main program
        while True:
            p = input("Enter YouTube Playlist URL: ")

            if p == "": # Exit
                print ("Thank You for using Python YouTube Playlist Downloader!")
                break

            purl = Playlist(p)

            print(f'Playlist Name: {purl.title_info}\n')

            for video in purl.videos:
                if video == "<pytube.__main__.YouTube object: videoId=sIBqmtI82c0>":
                    continue

                print(f"Downloading: {video.title}")
                print(f"\tVideo length: {timedelta (seconds = video.length)}\n")
                try:
                    st = video.streams.get_highest_resolution()
                    st.download(f"{path}\{PathNamer(purl.title_info)}")

                except OSError:
                    st = video.streams.get_highest_resolution()
                    st.download(f"{path}\{PathNamer(purl.title_info)}")

                # video.streams.first().download()
            
            print ("Playlist Downloaded Successfully!")

    if choice == 3:
        print (((" Thank you for using YouTube Downloader ").center (int (width * 0.9), "-")).center(width))
        print ("-"*width)

        break
