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
                    resultscolumn.append("new line" + ' = ' + str(k+1))
                else:
                    resultscolumn.append("'" + j + "'" + ' = ' + str(k))
            return "\n".join(resultscolumn)
        else:
            return "Enter any text"