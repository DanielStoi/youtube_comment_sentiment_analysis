"""
this is where everything is ran, or the user interface
"""
from sentiment_manager import * 
from sentiment_analysis import *
from youtube_comment_extractor import *

if __name__ == "__main__":
    print("this is the main application interface")
    print("STILL IN PROGRESS: but some basic functionality is already implemented")
    print("do not use for a video with alot of comments because it will likely surpass the free amount of api calls avaliable")
    print("in later versions; I plan to have a sentiment manager application that is able to more easily deal with more complex functionalities")
    print("-------------------------------")
    api = input("enter google api key: ")
    vid = extract_youtube_id(input("enter video id or url: "))
    while not vid:
        vid = extract_youtube_id(input("enter video id or url: "))

    s = sentiment_manager(api,vid)
    f = input("include entire file name for the sentiment value sheet: ")
    n = input("name of sentiment: ")
    
    s.import_sentiment_from_filename(f,f)
    s.generate_report(vid)
    
        
    
    
