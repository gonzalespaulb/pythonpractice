from bs4 import BeautifulSoup
import requests


# response = requests.get("https://news.ycombinator.com/news")
# response = requests.get("https://aspensnowmass.com/")
response = requests.get("https://sctconsulting.com.au/")
# response = requests.get("https://aspensciencecenter.org/")

yc_webpage = response.text
soup = BeautifulSoup(yc_webpage)

# print(soup.prettify())

# all_links = soup.find_all("a")

# for link in all_links:

#     link_directory = link.get("href")
#     # print(link.get("href"))
#     if "bike" in link_directory: 
#         print(link_directory)

all_svgs = soup.find_all("svg")

for svg in all_svgs: 
    
    svg_string = f"{svg}"
    replace_black = svg_string.replace('stroke="white"', 'stroke="black"')
    
    print(replace_black)
    # print(type(f"{svg}"))