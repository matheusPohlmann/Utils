from pytube import YouTube, Playlist

play = Playlist(
    'https://www.youtube.com/watch?v=D-fZXsPGBRk&list=PLCnM6_Q0Wz7TsUwjlkDqoO7A3wPhT3to-')

for pl in play.video_urls:
    d = YouTube(pl)
    video = d.streams.get_highest_resolution()
    filename = video.default_filename

    try:
        video.download(
            'youtube/videos',
            skip_existing=True,
        )
        print(filename)
    except:
        print(" NÃO DEU!!")
        pass
