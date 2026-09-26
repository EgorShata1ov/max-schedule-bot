from bs4 import BeautifulSoup

with open("group_page.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "lxml")

print("Элементы с временем")
for el in soup.find_all(string=lambda s: s and "8:15" in s):
    parent = el.parent
    print(f"\nТег: <{parent.name}>  Класс: {parent.get('class')}")
    print(f"Текст родителя: {parent.get_text(' ', strip=True)[:200]}")
    p = parent
    for i in range(3):
        p = p.parent
        if p is None:
            break
        print(f"  Уровень {i+1}: <{p.name}> class={p.get('class')} id={p.get('id')}")

print("\nУникальные CSS-классы (первые 40)")
classes = set()
for el in soup.find_all(True):
    for c in el.get("class", []):
        classes.add(c)
for c in sorted(classes)[:40]:
    print(" ", c)

print("\nЭлемент 'Понедельник'")
for el in soup.find_all(string=lambda s: s and "Понедельник" in s):
    parent = el.parent
    print(f"Тег: <{parent.name}>  Класс: {parent.get('class')}")
    print(f"Текст: {parent.get_text(' ', strip=True)[:200]}")
    print("Следующие 5 соседей:")
    for sib in parent.find_next_siblings()[:5]:
        print(f"  <{sib.name}> class={sib.get('class')}: {sib.get_text(' ', strip=True)[:150]}")
    break
