from bs4 import BeautifulSoup

with open("group_page.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "lxml")

item = soup.find("div", class_="sch-list-item")
print(item.prettify())
