# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 16:46:21 2023

@author: HP
"""

import json

# Opening JSON file
f = open('annotations.json', encoding="utf8")
  
# returns JSON object as 
# a dictionary
data = json.load(f)