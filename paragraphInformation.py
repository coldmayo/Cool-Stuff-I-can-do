paragraf=input("Input a paragraph")
x=len(paragraf)
print("There are",x,"characters used")
wordCount=0
print ("sentince count:"+str([paragraf.count(".")]))
for words in range(paragraf.count(".")):
    sen=paragraf[:paragraf.index(".")]
    if sen[0]==" ":
        wordCount+=sen.count(" ")
    else:
        wordCount+=sen.count(" ")+1
    paragraf[paragraf.index(".")+1:]
print ("word count is:"+str(wordCount))
