from bs4 import BeautifulSoup as bs
import requests
from colorama import Fore
url = "https://www.ua-football.com/ua/search?query=news"
response = requests.get(url)
beautifulsoup = bs(response.text, "lxml")

info = beautifulsoup.find_all("a", class_="liga-news-item-link")
info_titles = beautifulsoup.find_all("span", class_="fz-16 fw-500 d-block")
info_theme = beautifulsoup.find_all("span", class_="section-name fz-12")
info_date = beautifulsoup.find_all("li", class_="i_date gray")
index = 0

for title in info_titles:
    print("\n"+"\t"*20+Fore.RED+info_theme[index].text)
    print(Fore.BLACK+title.text)
    item_url = info[index].get("href")
    print("https://www.ua-football.com"+item_url)
    try:
        print(Fore.WHITE+info_date[index].text)
    except Exception:
        continue
    index+=1