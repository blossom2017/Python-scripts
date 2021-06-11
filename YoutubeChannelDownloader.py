from pytube import Youtube
from pytube import Channel
from slugify import slugify
import csv
import ffmpeg


def DownloadVideo(video_link, folder_path, resolution=None):
	if(resolution == None):
		video_file = Youtube(video_link).streams.order_by('resolution').desc().first().download()
	else:
		video_file = Youtube(video_link).streams.filter(res=resolution).order_by('resolution').desc().first().download()

	video_name = slugify(video_file.replace(".webm","").split("/")[-1])

	print("Video downloaded")

	audio_file = Youtube(video_link).streams.filter(only_audio=True).order_by('abr').desc().first().download(filename_prefix="audio_")

	print("Audio downloaded")

	source_audio = ffmpeg.input(audio_file)
	source_video = ffmpeg.input(video_file)
	ffmpeg.concat(source_video, source_audio, v=1, a=1).output(f"{folder_path}/{video_name}.mp4").run()

	print("Audio Video merging done")
	return None

def DownloadVideoFromChannel(channel_link, folder_path, resolution):
	channel = Channel(channel_link)
	for video_link in channel.video_urls[:3]:
		DownloadVideo(video_link, folder_path, resolution)
