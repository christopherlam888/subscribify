from video import Video
import pyfiglet
import requests
import multiprocessing
import tqdm
import webbrowser

def getVideos(channel):
    channel_videos = []
    url_start = 'https://vid.puffyan.us/api/v1/channels/'
    url_end = '?fields=author,authorId,latestVideos&pretty=1'
    response = requests.get(url = url_start+channel+url_end)
    data = response.json()
    for video in data['latestVideos']:
        channel_videos.append(Video(video['title'], data['author'], video['videoId']))
    return channel_videos

def main():

    # ASCII art
    print(pyfiglet.figlet_format('Subscribify'))

    # read channels file
    print("Reading file...")
    channels = []
    channels_file = open('channels.txt', 'r')
    while True:
        line = channels_file.readline().strip()
        if not line:
            break
        channels.append(line)
    channels_file.close()
    print("File read.")

    # get videos from API
    print("Getting videos...")
    videos = []
    with multiprocessing.Pool() as pool, tqdm.tqdm(total=len(channels)) as pbar:
        for channel_videos in pool.imap_unordered(getVideos, channels):
            videos.extend(channel_videos)
            pbar.update()
    print("Videos retrieved.")

    # print videos
    print()
    print("{:<5} {:<120} {:<30}".format("#", "Title", "Author"))
    i = 1
    for video in videos:
        print("{:<5} {:<120} {:<30}".format(i, video.title, video.author))
        i+=1

    # browsing
    url_start = 'https://vid.puffyan.us/watch?v='
    browsing = True
    while browsing:
        selection = input("Browsing...Enter an item number: ")
        if selection.isdigit() and int(selection) > 0 and int(selection) <= len(videos):
            print(f'URL:\n{url_start+videos[int(selection)-1].videoId}')
            webbrowser.open(url_start+videos[int(selection)-1].videoId, new=2)
        else:
            browsing = False

if __name__ == "__main__":
    main()
