import newspaper
import pandas as pd
from datetime import date
import re

def getArticles(website):
    ny_paper = newspaper.build(website)
    dict4df = dict()
    dict4df["url"] = list()
    dict4df["title"] = list()
    dict4df["text"] = list()
    dict4df["date"] = list()
    today = date.today()
    re_pattern = re.compile("religion|ritual|\bcult\b|purity|sacred|holy|religious", re.IGNORECASE)
    matches = 0
    print(f"Articles to search: {len(ny_paper.articles)}")

    for num, article in enumerate(ny_paper.articles):
        article.download()
        article.parse()
        #print(f"Downloading {num} article!")
        #print(f"Article title: { article.title }")
        if re_pattern.search(article.text):
            dict4df["url"].append(article.url)
            dict4df["title"].append(article.title)
            dict4df["text"].append(article.text)
            dict4df["date"].append(today)
            matches += 1

    df = pd.DataFrame.from_dict(dict4df)
    df.to_csv("religionml_newspaper.csv", header=False, mode="a")

    # STATUS

    with open("religionml_scraper_STATUS.txt", "a", encoding="utf-8") as f:
        f.write(f"{today}: Attempted to download {matches} articles!")
