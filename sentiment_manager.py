from sentiment_analysis import *
import youtube_comment_extractor
from comment_retreival_interface import *

class sentiment_manager:
    #sentiment manager is just an interface class for managing everything
    def __init__(self, api_key=None,youtube_video=list()):
        #note youtube video is the ID of the youtube video
        self.api_key = api_key
        if not type(youtube_video) == list:
            youtube_video = [youtube_video]
        self.youtube_videos = youtube_video
        self.sentiments = list()
        self.imported_comments = dict()

    def import_sentiment_from_filename(self,filename, name="unnamedSentiment"):
        if True:
            s = Sentiment(name)
            
            s.import_preferences(filename,True)
            
            self.sentiments.append(s)
            return True
        try:
            print("?")
        except:
            print("ERROR IMPORTING SENTIMENT")
            return False
            


    
    def pull_comments(self,vid_id):
        inter = generate_youtube_interface()
        inter.generic_features["google/youtube_api_key"] = self.api_key
        comments = inter.get({"vid_url":vid_id})
        #comments = youtube_comment_extractor.get_all_comments(self.api_key, vid_id, is_verbose=False)
        #comments = youtube_comment_extractor.flatten_list(comments)
        self.imported_comments[vid_id] = comments

        
    
    def generate_report(self,video_url,is_verbose=False):
        video_id = youtube_comment_extractor.extract_youtube_id(video_url)
        if not video_id in self.imported_comments:
            self.pull_comments(video_id)
            self.add_video(video_id)
                
        ans = []
        comments = self.imported_comments[video_id]
        
        for sen in self.sentiments:
            score = sen.generate_comments_scores_weighted(comments)
            ans.append((sen,score))
            print((str(sen),score))
        return ans

    def add_video(self,video_url):
        video_id = youtube_comment_extractor.extract_youtube_id(video_url)
        if not video_id in self.youtube_videos:
                self.youtube_videos.append(video_id)
    
                

if __name__ == "__main__":
    api = input("apikey: ")
    s =sentiment_manager()
    s.pull_comments(input("vid:"))
    
        
            
            
            
        
