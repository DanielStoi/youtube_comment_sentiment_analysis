


class Sentiment:

    def __init__(self, name="NONE", value_sheet = {}):
        self.name = str(name)
        self.value_sheet = value_sheet

    def __str__(self):
        return "[SENTIMENT:"+self.name+"]"

    def process_text(text):
        text = text.split()
        #text = text.split(".")
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
        return score/words
    
    def generate_comments_score_unweighted(self,comments,is_verbose=False):
        score = 0
        for comment in comments:
            val = self.calculate_score(comment[1])
            score+=val
            if is_verbose:
                print("score for",comment[0], "is",val)
        return score/len(comments)

    
    def generate_comments_scores_weighted(self,comments,is_verbose=False):
        score = 0
        for comment in comments:
            val = self.calculate_weighted_score(comment[1])
            score+=val
            if is_verbose:
                print("score for",comment[0], "is",val)
        return score/len(comments)
    
        
    def export_preferences(self, file_name):
        try:
            f = open(file_name,"w")
            for word in self.value_sheet:
                f.write(word+" "+str(self.value_sheet[word])+"\n")
                f.flush()
            f.close()
        except:
            errmsg = "in sentiment class; error exporting to file: "+str(file_name)
            raise Exception(errmsg)
        
    def import_preferences(self,file_name):
        if True:
            f = open(file_name,"r")
            lines = f.readlines()
            val_sheet = {}
            for i in lines:
                line = i.split(" ")
                val = float(line[-1])
                text = " ".join(line[:-1])
                val_sheet[text]=val
            print(val_sheet)
        try:
            print()
        except:
            errmsg = "in sentiment class; error inporting file: "+str(file_name)
            raise Exception(errmsg)


if __name__ == "__main__":
    print("running test for some random values")
    s = Sentiment("happness", {"red":-1,"yellow":5,"black":-1,"orange":1})
    print(s.calculate_weighted_score("yellow yellow black red orange yellow"))
    s.export_preferences("sentiment_export.txt")
    s.import_preferences("sentiment_export.txt")
    print(s.generate_comments_score_unweighted([["jeff","red blue black orange"],["joe","red red red red"],["bob","yellow yellow yellow"]],True))
    print(s)
