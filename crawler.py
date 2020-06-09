#AUTHOR : Uday Bhaskar kale
#Github username : koyana99
#run crawler.py first
#.csv and .log file will be created
#run scraper.py
#MODULE IMPORT from one .py file to another .py . will enhance the speed . TRY 
# or try to INVOKE scraper.py from crawler.py . will enhance the speed . TRY 
from urllib.error import HTTPError
from urllib.request import FancyURLopener
import  urllib.request			
from selenium import webdriver 	
import requests
import re
from csv import reader
import csv 
import bs4 as bs
import os


class FixFancyURLOpener(FancyURLopener):
	def http_error_default(self, url, fp, errcode, errmsg, headers):
		if errcode==403:
			raise ValueError("403")
		return super(FixFancyURLOpener, self).http_error_default(url, fp, errcode, errmsg, headers)

urllib.request.FancyURLopener = FixFancyURLOpener

class AppURLopener(urllib.request.FancyURLopener):	#set this according to your browser
	version ="mozilla/5.0" 
	
def urlopn(htmldocs):
	opener = AppURLopener()
	webopen = opener.open(htmldocs).read()
	soup=bs.BeautifulSoup(webopen,features="lxml") # lxml format for bs4 object 
	return soup

def google_query(query):
	 
	search_string = query.replace(' ', '+')  
	browser = webdriver.Firefox() 
	matched_elements = browser.get("https://www.google.com/search?q=" + search_string +"+song+download+free") #google query url format
	search_results = urlopn(browser.current_url) #parse google search page
	links = search_results.find_all('a')
	browser.quit()
	wl = [link['href'] for link in links if link['href'].startswith('/url?q=http')]  # find only references on google search results
	weblist = list()
	for x in wl:
		weblist.append(x[7:]) #removes '/url?q=http'
	csv_man(weblist) 
		
def csv_man(weblist):	
	with open("weblist.csv","w") as op:	# overwrite mode . try w+ or wb or r+
		writer = csv.writer(op, lineterminator='\n') # input in new row
		for val in weblist:	#	UTF-8	encoding of url
			x=val.replace('%3F','?').replace('%3D','=').replace('%26','&').replace('%25','%').replace('','').replace('%20',' ').replace('%21','!').replace('%22','"').replace('%23','#').replace('%24','$').replace(' 	%28','(').replace('%29',')').replace('%2B','+').replace('%2A','*').replace('%2C',',').replace('%2D','-').replace('%2E','.').replace('%2F','/')
			writer.writerow([x[:x.index("&sa")]])	#removes everything after countering '&sa'  

	
def main():
	query = input("\nInput the song :")
	weblist=google_query(query)
	
if __name__=="__main__":
	main()
	

print("\nNow Run scraper.py\n")
#saurabhghewande
