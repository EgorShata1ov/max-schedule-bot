import requests

BASE_URL = "https://www.istu.edu/schedule/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
}

print("?group=473847")
r = requests.get(BASE_URL, params={"group": 473847}, headers=headers, timeout=15)
print("Status:", r.status_code)
print("Final URL:", r.url)
print("Content-Length:", len(r.text))
print("Первые 1500 символов:\n")
print(r.text[:1500])

with open("debug_page.html", "w", encoding="utf-8") as f:
    f.write(r.text)
print("Полный HTML сохранён в debug_page.html")
