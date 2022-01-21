import sentiment_analysis
import youtube_comment_extractor

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

    def process_cmd(self,cmd):
        cmd = cmd.split()
        #TODO, this should actually just be moved to the main file

    def pull_comments(self,video_id):
        comments = youtube_comment_extractor.get_all_comments(get_api_key(), vid_id, is_verbose=False)
        comments = youtube_comment_extractor.flatten_list(comments)
        self.imported_comments[video_id] = comments

    
    def generate_report(self,video_url,is_verbose=False):
        video_id = youtube_comment_extractor.extract_youtube_id(video_url)
        if not video_id in self.imported_comments:
            self.pull_comments(video_id)
            self.add_video(video_id)
                
        ans = []
        comments = self.mported_comments[video_id]
        
        for sen in self.sentiments:
            score = sen.generate_comments_scores_weighted(comments)
            ans.append((sen,score))
            print((sen,score))
        return ans

    def add_video(self,video_url):
        video_id = youtube_comment_extractor.extract_youtube_id(video_url)
        if not video_id in self.youtube_videos:
                self.youtube_videos.append(video_id)
    
                

        
        
            
            
            
        
