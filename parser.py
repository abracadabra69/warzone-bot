import requests
from bs4 import BeautifulSoup

def get_meta_loadouts():
    url = "https://www.warzoneloadout.games/meta"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    loadouts = []

    for div in soup.find_all("div", class_="tier-list-weapon-card"):
        weapon_name = div.find("h3")
        if weapon_name:
            loadouts.append(weapon_name.text.strip())

        if len(loadouts) >= 5:
            break  # Берем топ-5

    if not loadouts:
        return "Не удалось получить мету. Сайт изменился или проблемы с подключением."

    return "Топ-мета:\n" + "\n".join([f"{i+1}. {w}" for i, w in enumerate(loadouts)])