import csv
import matplotlib.pyplot as plt


def create_pie(admin):
    if admin[1:] == ["0", "0", "0", "0"]:
        return
    nick = admin[0]
    values = admin[1:]
    labels = [
        f"Навсегда ({values[0]})",
        f"Истек ({values[1]})",
        f"Временно ({values[2]})",
        f"Разбанен ({values[3]})",
    ]
    colors = ["#F8333C", "#FCAB10", "#2B9EB3", "#44AF69"]
    explode = (0.1, 0, 0, 0)
    plt.pie(
        values,
        explode=explode,
        colors=colors,
    )
    plt.title(nick)
    plt.legend(labels)
    plt.savefig(f"./pies/{nick}.png", dpi=300)
    plt.show()
    plt.close()


with open("stats.csv", "r") as stats_file:
    for item in csv.reader(stats_file):
        create_pie(item)
