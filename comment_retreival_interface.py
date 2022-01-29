"""
comment_retreival_interface is just an abstraction for the retreival methods of comments.
it can in theory support more than just rest apis but also stateful connections such as sockets

the idea is that for example a twitter api for comments, a socket based connection for reading comments,
youtube comments can all be easily handled within the main functionality by 
defining the arguments for initialising and retreiving comments from some source
then the retreival methods are hidden though the "get_fct" method
"""

def empty_method(self,a):
    pass
    
def input_check_wrap(fct,args):
    def new_fct(self,a):
        if not a.keys() == args.keys():
            raise Exception("error with inputs of function: "+str(a.keys())+" instead of "+str(args.keys()))
        assert type(a)==dict
        return fct(self,a)
    return new_fct


class comment_retreival_interface:
    #an abstraction of the connection interface
    #generic_ are generic features relating to connecting to the API (eg: api key)
    #page_features are the individual feature for connecting to each "page" of comments
    #init_fct is if a connection needs to be established beforehand (eg: with sockets)
    #get_fct is the function for getting a "page" of comments given certain "feature" arguments
    def __init__(self,generic_features,page_features,get_fct,init_fct=empty_method):
        assert type(generic_features) == dict
        assert type(page_features) == dict
        assert callable(init_fct) and callable(get_fct)
        self.generic_features = generic_features
        self.page_features = page_features
        self.init_fct = input_check_wrap(init_fct,generic_features)
        self.get_fct = input_check_wrap(get_fct,page_features)
        self.help_str = "NO HELP STRING"
    def get(self,args):
        return self.get_fct(self,args)


def generate_youtube_interface():
    #TODO: add max pages/comments functionality
    import youtube_comment_extractor
    api_name = "google/youtube_api_key"
    id_name = "vid_url"
    generic = {api_name:None}
    get ={id_name:None}#,"max_pages"]

    def get_comments(self,args):
        api = self.generic_features
        vid = youtube_comment_extractor.extract_youtube_id(args[id_name])
        comments = youtube_comment_extractor.get_all_comments(self.generic_features[api_name], vid, is_verbose=False)
        comments = youtube_comment_extractor.flatten_list(comments)
        return comments
        
    yt = comment_retreival_interface(generic,get,get_comments)
    return yt