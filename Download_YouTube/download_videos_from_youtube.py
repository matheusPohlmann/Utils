from pytube.cli import on_progress
from pytube import YouTube

# Obviamente, antes de rodar o código confira se o pytube está instalado.
# Caso não esteja, abra o terminal e digite 'pip install pytube'.

urls = [
    # Coloque aqui as urls dos videos que quer baixar.
]

for url in urls:

    yt = YouTube(url, on_progress_callback=on_progress)
    video = yt.streams.get_highest_resolution()
    filename = video.default_filename

    try:
        video.download(
            # aqui nas aspas simples, você coloca o caminho do diretório onde deseja guardar os videos.
            # Como default, eu crio o diretório 'youtube/videos'.
            'youtube/videos',
            skip_existing=True,
        )
        print(filename)
    except:
        print(" NÃO DEU!!")
        pass
