import pymongo
from difflib import get_close_matches
from pymongo import MongoClient 
import array
def translate(w):
    data = MongoClient("mongodb+srv://vidhya-spellcheck:Ansel17@spellcheck.hfwpm.mongodb.net/vidhya-spellcheck?retryWrites=true&w=majority")
    db=data["names"]
    collection=db["name-spellcheck"]
    results=collection.find({})
    for x in results:
        keys = x.keys()
        y=[]
        for k in x.values():
    	    y.append(k)
    x=y[1:len(y)] #array of values in database
    flag=0
    for j in range(len(y)):
        if(w==y[j]):
            flag=1
            #print("word exists")
    if(flag==1):
        print("name exists")
    else:
        print("Did u mean:")
        print(get_close_matches(w, x,n=2,cutoff=0.6))
        print("not exits")

word = input("Enter name: ")
output = translate(word)
