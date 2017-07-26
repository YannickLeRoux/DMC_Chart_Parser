#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Jul 21st 2017

@author: yannickleroux

The purpose of this program is to parse the 'buzz chart - day' of the website
and try to find zippyshare download links for the charted tracks.

You'll need Firefox installed and the latest version of geckodriver 
installed in PATH

"""
from bs4 import BeautifulSoup
import requests
import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

urlstart="http://www.dmcworld.net/features/charts/buzz-chart/buzz-charts-25-05-17/"
response = requests.get(urlstart,headers={'User-Agent': 'Mozilla/5.0'})
results_page = BeautifulSoup(response.content, 'lxml')
real_url = results_page.find('iframe',{'id':'buzzframe'})
url = real_url.get('src')

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get(url)

elm = driver.find_elements_by_class_name("track-title")

for track in elm[:20]:
    new = 2
    tabUrl = "http://google.com/search?q="
    term = track.text + "+zippyshare" # searching for matching zippyshare links
    webbrowser.open(tabUrl + term,new = new)

# driver.close()
        
