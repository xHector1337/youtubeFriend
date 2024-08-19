from pytube import YouTube
from os import getcwd
def MP4LowestResolution(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension="mp4").get_lowest_resolution()
        stream.download(output_path=getcwd())
    except Exception as e:
        if e == "get_throttling_function_name: could not find match for multiple":
            print(f"{e} error! Check https://github.com/pytube/pytube/issues/1954 for solution!")
        else:    
            print(f"Error: {e}")    
MP4LowestResolution("https://youtu.be/ss6lhSwb-u8")
def MP4HighestResolution(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension="mp4").get_highest_resolution()
        stream.download(output_path=getcwd())
    except Exception as e:
        if e == "get_throttling_function_name: could not find match for multiple":
            print(f"{e} error! Check https://github.com/pytube/pytube/issues/1954 for solution!")
        else:
            print(f"Error {e}")
def MP4OnlyAudio(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        stream.download(output_path=getcwd())
    except Exception as e:
        if e == "get_throttling_function_name: could not find match for multiple":
            print(f"{e} error! Check https://github.com/pytube/pytube/issues/1954 for solution!")
        else:
            print(f"Error {e}")
MP4OnlyAudio("https://www.youtube.com/watch?v=YW_ucgRrW6w")                                                
