


class Sentiment:

    def __init__(self, name="NONE", value_sheet = {}):
        self.name = name
        self.value_sheet = value_sheet

    def process_text(text):
        text = text.split(" ")
        text = text.split(".")
        t = []
        for i in text:
            if i:
                t.append(i)
        return t
        
    def calculate_score(self, text):
        score=0
        for word in self.value_sheet:
            if word in text:
                score += text.count(word)*self.value_sheet[word]
        return score
            
        
        
        
        

    def calculate_weighted_score(self, text):
        score=0
        words = len(Sentiment.process_text(text)) # amount of distinct words
        for word in self.value_sheet:
            if word in text:
                score += text.count(word)*self.value_sheet[word]
        return score
        
        
        
    
