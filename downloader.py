# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 17:10:38 2023

@author: HP

# imported the requests library
import requests
image_url = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"
  
# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url) # create HTTP response object
  
# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("python_logo.png",'wb') as f:
  
    # Saving received content as a png file in
    # binary format
  
    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.write(r.content)
    
    
# -*- coding: utf-8 -*-
Created on Tue Apr  4 13:28:30 2023

@author: Rez
"""

from rdflib import Graph

import sys
import requests

entities = []
description = []
sourceFile = open('productListFinal.txt', "w", encoding="utf-8")



for i in range(300):
    
    #http://www.productontology.org/dump.rdf?limit=x&offset=y


    url = "http://www.productontology.org/dump.rdf?limit=1000&offset="
    url = url + str(i*1000)
    
    r = requests.get(url) # create HTTP response object
    with open("dump.rdf",'wb') as f:
        f.write(r.content)
    
    g = Graph()
    g.parse("dump.rdf")
    
    counter = 0
    
    for stmt in g:
    
        counter = counter + 1
        url = stmt[0]
        #print(url)
        
        import urllib.request
        
        try:
            file = urllib.request.urlopen(url)
        except Exception as e:
            continue
        
        
        current_keyword = ""
        current_description = ""
    
        if("%" in url):
            continue
        
        if("/id/" in url):
            temp = current_keyword = url.split("/id/")
            if(len(temp) < 2):
                continue
            current_keyword = url.split("/id/")[1]
        else:
            temp = current_keyword = url.split("/doc/")
            if(len(temp) < 2):
                continue
            current_keyword = url.split("/doc/")[1]
        
    
        print(current_keyword, file = sourceFile)
        if(counter % 100 == 0):
            print(i)
            print(counter)
    
    
    


sourceFile.close()

    
