#This code is to present function that count all characters (including whitespaces) in any text provided by variable <anytext>.
#For each character the number of its occurrences in the text is calculated and given on a separate line
#Returns sorted results: chartxtcount(anytext, arg)
#<arg> value is optional. A Boolean. False will sort ascending, True will sort descending. Default is False
#Dictionary methods were used.

class CharacterCounter:
    
    def __init__(self, text):
        self.text = text
        self.lenght_of_text = 0

    def chartxtcount(self, arg=False):
        septext = "".join(self.text)
        dic = {}
        resultscolumn = []
        if self.text:
            for i in sorted(septext,reverse=arg):
                dic.setdefault(i, self.text.count(i))
                if i != "\n":
                    self.lenght_of_text+=1
            for j,k in dic.items():
                if j == "\n":
                    resultscolumn.append("Paragraphs" + ' = ' + str(k+1))
                else:
                    resultscolumn.append("'" + j + "'" + ' = ' + str(k))
            return "\n".join(resultscolumn)
        else:
            return "Enter any text"