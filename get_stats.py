from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import csv
import re
from math import ceil
from time import sleep


def get_number_of_pages(admin):
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    }

    name, id = admin
    sleep(0.5)
    url = (
        f"https://jumpclassic.ru/bans/index.php?p=banlist&advSearch={id}&advType=admin"
    )
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.text, "lxml")
    data = soup.find("div", class_="card-header")
    small = data.find("small")
    total = small.text.strip().split(":")[1]
    total = int(re.search(r"\d+", total).group())
    return ceil(total / 30)


def get_stats(admin):
    name, id = admin

    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    }
    pages = [i for i in range(1, get_number_of_pages(admin) + 1)]
    stats = {"Навсегда": 0, "Истек": 0, "Временно": 0, "Разбанен": 0}

    for page in pages:
        sleep(0.5)
        url = f"https://jumpclassic.ru/bans/index.php?p=banlist&page={page}&advSearch={id}&advType=admin"
        r = requests.get(url, headers=header)

        soup = BeautifulSoup(r.text, "lxml")
        data = soup.find_all("tr", class_="opener")
        for item in data:
            key = item.find_all("td")[-1].text.strip()
            if key in stats.keys():
                stats[key] += 1
            else:
                stats["Временно"] += 1

    return list(stats.values())


with open("sb_ids.csv", "r") as ids_file:
    with open("stats.csv", "a") as stats_file:
        writer = csv.writer(stats_file)
        for item in csv.reader(ids_file):
            print(item, end="\t")
            print("in progress...")
            writer.writerow([item[0]] + get_stats(item))
            print("Success!")
