from asyncore import write
from bs4 import BeautifulSoup
import requests
import csv


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
}
r = requests.get("https://jumpclassic.ru/bans/index.php?p=search_bans", headers=header)
soup = BeautifulSoup(r.text, "lxml")

data = soup.find("select", {"id": "ban_admin"})


with open("sb_ids.csv", "a") as f:
    writer = csv.writer(f)
    for option in data.find_all("option"):
        writer.writerow([option["label"], option["value"]])
