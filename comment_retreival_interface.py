

class comment_retreival_interface:
    #an abstraction of the connection interface
    #generic_ are generic features relating to connecting to the API (eg: api key)
    #page_features are the individual feature for connecting to each "page" of comments
    #init_fct is if a connection needs to be established beforehand (eg: with sockets)
    #get_fct is the function for getting a "page" of comments given certain "feature" arguments
    def __init__(self,generic_features,page_features,get_fct,init_fct=empty_method):
        assert (type(generic_features)==dict and type(page_features)==dict())
        assert(callable(init_fct) and callable(get_fct))
        self.generic_features = generic_features
        self.page_features = page_features
        self.init_fct = init_fct
        self.retr_fct = retr_fct


def generate_youtube_interface:
    import youtube_comment_extractor
    #TODO
    
    
