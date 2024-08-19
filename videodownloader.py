from pytube import YouTube
from os import getcwd
import pathlib
import argparse
def MP4LowestResolution(url,path="None"):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension="mp4").get_lowest_resolution()
        if path == "None":
            stream.download(output_path=getcwd())
        else:
            stream.download(output_path=path)    
    except Exception as e:
        if e == "get_throttling_function_name: could not find match for multiple":
            print(f"{e} error! Check https://github.com/pytube/pytube/issues/1954 for solution!")
        else:    
            print(f"Error: {e}")    
MP4LowestResolution("https://youtu.be/ss6lhSwb-u8")
def MP4HighestResolution(url,path="None"):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension="mp4").get_highest_resolution()
        if path == "None":
            stream.download(output_path=getcwd())
        else:
            stream.download(output_path=path)    
    except Exception as e:
        if e == "get_throttling_function_name: could not find match for multiple":
            print(f"{e} error! Check https://github.com/pytube/pytube/issues/1954 for solution!")
        else:
            print(f"Error {e}")
def MP3(url,path="None"):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        ohmygotto = ""
        if path == "None":
            stream.download(output_path=getcwd())
            ohmygotto = pathlib.Path(stream.get_file_path())
        else:
            stream.download(output_path=path)       
            ohmygotto = pathlib.Path(f"{path}{yt.title}.mp4")
        ohmygotto.rename(ohmygotto.with_suffix(".mp3"))
    except Exception as e:
        if e == "get_throttling_function_name: could not find match for multiple":
            print(f"{e} error! Check https://github.com/pytube/pytube/issues/1954 for solution!")
        else:
            print(f"Error {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url",help="Url of video to be downloaded.")
    parser.add_argument("filetype",help="Specify file type as mp4 file.(mp4/mp3)")
    parser.add_argument("--lowestresolution",help="Specify video resolution as the lowest.",action="store_true")
    parser.add_argument("--path",help="Specify download path. It uses current working directory as default.")
    args = parser.parse_args()
    if args.url and "https" and ("youtube.com" or "youtu.be") in args.url:
        if args.filetype == "mp4" and args.path and not args.lowestresolution:
            MP4HighestResolution(args.url,args.path)
        elif args.filetype == "mp4" and args.path and args.lowestresolution:
            MP4LowestResolution(args.url,args.path)
        elif args.filetype == "mp4" and not args.path and not args.lowestresolution:
            MP4HighestResolution(args.url)
        elif args.filetype == "mp3" and not args.path:
            MP3(args.url)
        elif args.filetype == "mp3" and args.path:
            MP3(args.url,args.path)
        else:
            print("Unsupported method found.")
    else:
        print("Enter an YouTube url.")
main()                                             
        
