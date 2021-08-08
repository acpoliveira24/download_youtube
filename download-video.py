from pytube import YouTube


# Armazena o link do vídeo a ser baixado
link = input("Insira o link do vídeo: ")
video = YouTube(link)

print(f"Nome do vídeo: {video.title}")

# Seleciona a maior resolução disponível
video_resolution = video.streams.get_highest_resolution()

video_resolution.download()

print("Download completo!")
