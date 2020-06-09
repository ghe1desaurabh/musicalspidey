#AUTHOR : Uday Bhaskar kale
#Github username : koyana99
#run crawler.py first
#.csv and .log file will be created
#run scraper.py
#MODULE IMPORT from one .py file to another .py , will enhance the speed . Try !
#If you give input song with website names , this will improve google search indexing 
#if you dont jiosaavn , gaana , hungama like useless searches will be handled by machine , so utter time waste 
#for e.g. : Mala ved lagale djmarathi.in 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import  urllib.request 
import bs4 as bs
from urllib.error import HTTPError
from urllib.request import FancyURLopener
import requests
import re
from csv import reader
import csv 
import time
import os
import pyautogui
pyautogui.PAUSE = 2.5

class AppURLopener(urllib.request.FancyURLopener):
	version ="mozilla/5.0" 
	
def urlopn(htmldocs):
	opener = AppURLopener()
	webopen = opener.open(htmldocs).read()
	soup=bs.BeautifulSoup(webopen,features="lxml")
	return soup
	
def scraper():
	with open(os.path.expanduser('~') + '/Desktop/weblist.csv', 'r') as ip:	#path setting for your os + location of csv file , in read mode
		csv_reader = reader(ip)
		for row in csv_reader:
			try:
				soup = urlopn(row[0])	#row is length parameter and row[digit] is value . soup is bs4 object
				sources = soup.find_all('source') #finds all tags with source
				srclist= list()
				for x in sources :
						srclist.append(x['src']) #attribute of source 
				download(srclist)
			except urllib.error.HTTPError :
				print("HTTP socket error !")	
		print("\nEnd of csv_reader")

def download(srclist):
	for x in srclist:
		if 'mp3' in x :
			driver = webdriver.Firefox()	#selenium Firefox object
			matched = driver.get(x)
			pyautogui.click(x=680, y=415,button='right')	# pyautogui for GUI manipulation
			pyautogui.click(x=720, y=545,button='left')
			pyautogui.press('enter')
			if download_wait()== 'downloaded':		#remove if downloaded_wait() is removed 
				driver.quit()

def download_wait(): #machine will get slower bcoz of this , u can remove this function 
	download_path="/home/kale/Downloads"		#linux file system . will be different in your case
	wait= True
	while wait :
		for fname in os.listdir(download_path):	#finds directories in "Download/"
			if fname.endswith('mp3'):
				wait = False
				x = 'downloaded'
		time.sleep(60*2)
	return x 
	
def main():
	scraper()	
	
if __name__=="__main__":
	main()
	

