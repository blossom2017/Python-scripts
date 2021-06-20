from pytube import YouTube
from pytube import Channel
from slugify import slugify
import os
import csv
import sys
import ffmpeg


def DownloadVideo(video_link, folder_path, resolution=None):
    print("Starting Video download")
    # TODO(Add exception handling in case http requests failed & return boolean value true or false for success)
    # TODO(Delete the webm files)
    if(resolution == None):
        video_file = YouTube(video_link).streams.order_by(
            'resolution').desc().first().download()
    else:
        video_file = YouTube(video_link).streams.filter(
            res=resolution).order_by('resolution').desc().first().download()

    video_name = slugify(video_file.replace(".webm", "").split("/")[-1])

    print("Video downloaded")

    print("Starting Audio download")
    audio_file = YouTube(video_link).streams.filter(only_audio=True).order_by(
        'abr').desc().first().download(filename_prefix="audio_")
    print("Audio downloaded")

    print("Starting audio video merging")
    source_audio = ffmpeg.input(audio_file)
    source_video = ffmpeg.input(video_file)
    video_file_output_path = folder_path + "/" + video_name + ".mp4"
    ffmpeg.concat(source_video, source_audio, v=1, a=1).output(
        f"{video_file_output_path}").run()
    print("Audio Video merging done")

    return None


def DownloadVideoFromChannel(channel_link, folder_path, resolution):
    channel = Channel(channel_link)
    list_of_videos_downloaded = []
    youtube_history_filename = 'youtube_videos_downloaded_history.csv'
    if not os.path.exists(youtube_history_filename):
        csvfile = open(youtube_history_filename, 'w')

    # Open in read mode
    with open(youtube_history_filename, 'r', newline='') as csvfile:
        all_rows = csv.reader(csvfile)
        for row in all_rows:
            list_of_videos_downloaded.append(row[0])

    # print(list_of_videos_downloaded)

    for video_link in channel.video_urls:
        if video_link in list_of_videos_downloaded:
            print('Video already existing')
        else:
            DownloadVideo(video_link, folder_path, resolution)
            with open(youtube_history_filename, 'a+', newline='') as csvfile:
                all_rows = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
                all_rows.writerow([video_link])
            print('Video done')


"""
Command line usage - python YoutubeChannelDownloader.py channel_link folder_link resolution
python3 YoutubeChannelDownloader.py https://www.youtube.com/c/SkyGuitar/videos YoutubeVideos 1080p
"""


def main(argv):
    DownloadVideoFromChannel(argv[0], argv[1], argv[2])


if __name__ == "__main__":
    main(sys.argv[1:])
