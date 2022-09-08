import requests
from beautifulsoup import bs4 as bs
r = requests.get('https://store.standoff2.com/ru/profile/12312312')
soup = bs(r.text, "html.parser")
print(soup.findAll("div", class_="MuiBox-root jss10"))
