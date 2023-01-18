from video import Video
import istarmap

import pyfiglet
import argparse
import requests
import multiprocessing
import tqdm
import webbrowser

INSTANCE = 'y.com.sb'

def parse_args():
    parser = argparse.ArgumentParser(description="Available Options")
    parser.add_argument('-n', '--number_videos', dest='number_videos')
    args = vars(parser.parse_args())
    return args

def getVideos(channel, n):
    channel_videos = []
    url_start = f'https://{INSTANCE}/api/v1/channels/'
    url_end = '?fields=author,authorId,latestVideos&pretty=1'
    response = requests.get(url = url_start+channel+url_end)
    data = response.json()
    for video in data['latestVideos'][:n]:
        channel_videos.append(Video(video['title'], data['author'], video['published'], video['videoId']))
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
    args = parse_args()
    if args['number_videos']:
        n = abs(int(args['number_videos'].strip()))
    else:
        n = 1
    with multiprocessing.Pool() as pool:
        params = [(channel, n) for channel in channels]
        for channel_videos in tqdm.tqdm(pool.istarmap(getVideos, params), total=len(channels)):
            videos.extend(channel_videos)
    print("Videos retrieved.")

    # sort videos by published
    videos.sort(key=lambda video: video.published, reverse=True)

    # print videos
    print()
    print("{:<5} {:<120} {:<30}".format("#", "Title", "Author"))
    for i, video in enumerate(videos):
        print("{:<5} {:<120} {:<30}".format(i+1, video.title, video.author))

    # browsing
    url_start = f'https://{INSTANCE}/watch?v='
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
