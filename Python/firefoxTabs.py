#! /usr/bin/python
'''
  firefoxTabs.py 
  Usage: Saves current Firefox tabs from clipboard to file or reads URLs
         from file and opens each in a separate tab in Firefox.    
'''
import os, sys, pyperclip, webbrowser, bs4

mylibrary = os.environ['MYPYTHONLIB']
sys.path.append(mylibrary)
import dtg

# Read URLs from clipboard or from file
if len(sys.argv) == 1:
    mode = 'write'    # write the URLs to file and exit
    urls = pyperclip.paste()
    # TODO: Check if urls.txt exists and move to urls_(dtg.dtg()).txt.
    urlsFile = open('/home/jim/bin/urls.txt', 'w')
    urlsFile.write(urls)
    urlsFile.close()
    sys.exit()
else:
    # TODO: Use argparse to check supplied options
    mode = 'read'
    try:
        urlsFile = open(sys.argv[1], 'r')
    except:
        urlsFile = open('/home/jim/bin/urls.txt', 'r')
    urls = urlsFile.read()
        
# Parse URLs with Beautiful Soup
urlSoup = bs4.BeautifulSoup(urls)
for link in urlSoup.find_all('a'):
    # Open a browser tab for each URL found.      
    #webbrowser.open(str(link.get('href')))
    webbrowser.open(link.get('href'))

urlsFile.close()
