# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests
import json
import re

reuters="https://newsapi.org/v1/articles?source=reuters&sortBy=top&apiKey=990d579b0b444038904c73627b57c5ff"

    
def headlines(url):
    r=requests.get(url)
    titles=[]
    for i in range(1,len(json.loads(r.content)['articles'])):
        titles.append(json.loads(r.content)['articles'][i]['title'])
    return(titles)
        
print(headlines(reuters))

[re.search("[wW]idow",a) is not None for a in headlines(reuters)]

#feature vector: capitalization, frequency across bbc/reuters, not_US_not_filler

#def contain_word(word):
    #use grepl to see if headlines contain word, count number of headlines which do
    
