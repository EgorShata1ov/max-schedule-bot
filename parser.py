import requests
from bs4 import BeautifulSoup
import json

GROUP_ID = 478015
BASE_URL = f"https://www.istu.edu/raspisanie/grup/{GROUP_ID}/"


def parse_schedule(url: str = BASE_URL) -> list[dict]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }
    r = requests.get(url, headers=headers, timeout=15)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")

    lessons = []
    current_day = None

    for el in soup.find_all(["h2", "div"]):
        classes = el.get("class", [])

        if "sch-list-day-header" in classes:
            current_day = el.get_text(" ", strip=True)
            continue

        if "sch-list-item" not in classes or current_day is None:
            continue

        time_el = el.find("div", class_="sch-list-item-time-inner")
        time_str = time_el.get_text(strip=True) if time_el else ""

        for week_div in el.find_all("div", class_="sch-list-item-week"):
            week_classes = week_div.get("class", [])
            if "week-even" in week_classes:
                week = "even"
            elif "week-odd" in week_classes:
                week = "odd"
            else:
                week = ""

            for card in week_div.find_all("div", class_="schcls-item"):
                if "schcls-empty" in card.get("class", []):
                    continue

                name_el = card.find("div", class_="schcls-item-name")
                type_el = card.find("div", class_="schcls-item-distype")
                prepod_el = card.find("div", class_="schcls-item-prepod")
                group_el = card.find("div", class_="schcls-item-group")
                aud_el = card.find("div", class_="schcls-item-aud")

                subject = name_el.get_text(strip=True) if name_el else ""
                ltype = type_el.get_text(strip=True) if type_el else ""
                teacher = prepod_el.get_text(strip=True) if prepod_el else ""
                room = aud_el.get_text(strip=True) if aud_el else ""
                groups = [a.get_text(strip=True) for a in group_el.find_all("a")] if group_el else []

                lessons.append({
                    "day": current_day,
                    "time": time_str,
                    "week": week,
                    "subject": subject,
                    "type": ltype,
                    "teacher": teacher,
                    "groups": groups,
                    "room": room,
                })

    return lessons


if __name__ == "__main__":
    data = parse_schedule()
    print(json.dumps(data, ensure_ascii=False, indent=2))