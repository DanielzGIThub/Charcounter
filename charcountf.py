#This code is to present function that count all characters (including whitespaces) in any text provided by variable <anytext>.
#For each character the number of its occurrences in the text is calculated and given on a separate line
#Returns sorted results: chartxtcount(anytext, arg)
#<arg> value is optional. A Boolean. False will sort ascending, True will sort descending. Default is False
#Dictionary methods were used.

def chartxtcount(text, arg=False):
    septext="".join(text)
    dic= {}
    resultscolumn=''
    for i in sorted(septext,reverse=arg):
        dic.setdefault(i, text.count(i))
    for j,k in dic.items():
        resultscolumn+="'"+j+"'"+' = '+str(k)+'\n'
    return resultscolumn

