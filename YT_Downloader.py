from pytube import YouTube

#to get the video link
def video_link():
    link = input("Enter the video link:")
    return link

#function to exit program
def exit_program():
    asdw = input("Pressed any to exit:")
    quit()

#here can add some command to verify this 'video_link()'is 'https://'or not
#of course if you add this,you will have to solve some bugs
yt = YouTube (video_link())

#to verify this link have video or not
def verify():
    try:
        d_video = yt.streams.get_highest_resolution ()
        return True
    except Exception:
        print('Unknown URL ')
        print('Please try again')
        return False

#to download video
def download_video():
    if verify()== True:
        try:
            d_video = yt.streams.get_highest_resolution ()
            d_video.download()
        except:
            print("Some Error!")
            print("Please try again!")
            exit_program()
    else:
        print("Some Error!")
        print("Please try again!")
        exit_program()

if __name__ == '__main__':
    download_video()