# -*- coding: utf-8 -*-
"""
Created on Sun May 16 13:55:32 2021

@author: Sumi
"""


import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/Sumi/Desktop/salary_proj/chromedriver"
df = gs.get_jobs('Data Science', 15, False, path, 5)