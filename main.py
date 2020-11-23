from scraper import getArticles

if __name__ == "__main__":
    newspaper_url_list = [
        "https://www.spiegel.de/",
        "https://edition.cnn.com/",
        "https://www.nytimes.com/"
    ]

    print("Downloading and processing articles...")
    for website in newspaper_url_list:
        getArticles(website)
    print("... done!")
