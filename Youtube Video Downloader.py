# you need to download pyyube module

from pytube import YouTube

link = "https://www.youtube.com/watch?v=pTFZFxd4hOI&t=226s&ab_channel=ProgrammingwithMosh"

youtube_1 = YouTube(link)


print(youtube_1.title)
print(youtube_1.author)
print(youtube_1.thumbnail_url)
#=========================================
# videos = youtube_1.streams.all() # This will give you all the formats
# videos = youtube_1.streams.all()
videos = youtube_1.streams.filter(only_audio=True)
videos_streaming_list = list(enumerate(videos)) # list has index number and enumerate store this
for i in videos_streaming_list:
    print(i)

print()
print()

strm = int(input("Enter :"))
videos[strm].download()
print('Downloaded Successfully')


