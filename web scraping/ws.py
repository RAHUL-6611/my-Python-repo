# If you wan to scrape a website

# Step 0
# install the requirement
# 1.html5lib
# 2.bs4
# 3.requests

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Step 1. Get the HTML
r = requests.get(url)
htmlContent = r.content
print(htmlContent)
# exit()

# Step 2. Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
print(soup.prettify)


# Step 3. HTML Tree traversal
#
# commonly used types of objects:
# 1.Tag
# 2.NavigableString
# 3.BeautifulSoup
# 4. Comment

# Get the title of the HTML page
title = soup.title
# print(type(title))        # 1.Tag.
# print(type(soup))         # 3.BeautifulSoup.
# print(type(title.string)) # 2.NavigableString.

# Get all the paragraphs from the page
paras = soup.find_all('p')
print(paras)


# Get first element of the HTML page
print(soup.find('p'))
# get their classes
print(soup.find('p')['class'])

# find all the element in class lead
print(soup.find_all("p", class_="lead"))

# -----------------------------------------------------------------
# get the text from the tags/soup
print(soup.find("p").get_text())

# print(soup.get_text())       //whole html text (:


# Get all the anchors from the page
anchors = soup.find_all('a')
print(anchors)

all_linksinthis = set()                           #list,set,tuple   but set is better in this case
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'):
        # print(link.get('href'))
        links = "https://codewithharry.com" + link.get('href')
        all_linksinthis.add(links)
        # print(links)                            #print in normal manner
        print(all_linksinthis)                    # print in set manner


# markup = <p