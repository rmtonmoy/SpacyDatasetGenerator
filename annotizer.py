# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 13:28:30 2023

@author: Rez
"""

from rdflib import Graph

entities = []
description = []
sourceFile = open('trainData100.txt', "a", encoding="utf-8")


g = Graph()
g.parse("dump.rdf")

counter = 0

for stmt in g:
    #pprint.pprint(stmt)
    #print("\n\n")
    counter = counter + 1
    if counter < 100:
        continue

    
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
    
    if("." in current_keyword):
        continue
    
    commentTagFound = False
    pTagFound = False
    with open('output.txt', 'w', encoding="utf-8") as f:
        for line in file:    
            decoded_line = line.decode("utf-8")
            if("(Source: Wikipedia" in decoded_line):
                commentTagFound = False
                pTagFound = False
            
            if("<div class=\"comment\">" in decoded_line):
                commentTagFound = True
            
            if(commentTagFound == True):
                if("<p>" in decoded_line):
                    pTagFound = True
                
                if(pTagFound == True):
                    if("<p>" in decoded_line):
                        decoded_line = decoded_line.split("<p>")[1]
                    #f.write(decoded_line)
                    current_description = current_description + decoded_line
                    
    
    #print(current_keyword)
    #print(current_description)
    
    #entities.append(current_keyword)
    #description.append(current_description)
    
    potential_aliases = []
    potential_aliases.append(current_keyword)
    if("_" in current_keyword):
        potential_aliases.append(current_keyword.replace("_", " "))
        if (current_keyword.count("_") >= 2):
            initials = ""
            for words in current_keyword.split("_"):
                initials = initials + words[0]
            
            potential_aliases.append(initials)
    
    
    

    line = current_description.split(".")
    for str in line:
        str = str.replace('\n', '')
        #while(len(str) >= 1 and str[0] == ' '):
           #str = str.replace(' ', '')

                
        formatted_output = "(\""
        formatted_output = formatted_output + str + ".\", {\"entities\": "
        
        locs = []
        for pattern in potential_aliases:
            starts = 0
            if(str.lower().find(pattern.lower(), starts) != -1):
                starts = str.lower().find(pattern.lower(), starts)
                add = 0
                if(starts+len(pattern) < len(str)):
                    if(str[starts+len(pattern)] == ' '):
                        add = 1
                        
                locs.append( (starts, starts + len(pattern) - 1 + add, 'PRODUCT') )
                starts = starts + 1
                
        
        if(len(locs) > 0):
            print(formatted_output, end = "", file = sourceFile)
            print(locs, end = "}),", file = sourceFile)
            #("I use a hammer to drive nails.", {"entities": [(9, 15, "PRODUCT")]}),
        
    #print(counter)
    print(current_keyword)
    
    if(counter == 200):
        break
    


sourceFile.close()

    
