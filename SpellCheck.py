import pymongo 
from pymongo import MongoClient 
import array
def translate(w):
    data = MongoClient("mongodb+srv://vidhya-spellcheck:Ansel17@spellcheck.hfwpm.mongodb.net/vidhya-spellcheck?retryWrites=true&w=majority")
    db=data["names"]
    collection=db["name-spellcheck"]
    results=collection.find({})
    for x in results:
        #print(x)
        keys = x.keys()
        y=[]
        for k in x.values():
	    #i=i+1
    	    y.append(k)
    	#w=w.lower()
    flag=0
    for j in range(len(y)):
        if(w==y[j]):
            flag=1
    if(flag==1):
        print("word exist")
    else:
        print("not exist")
word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
