import pandas as pd
import urllib.request
import wget
import sys
import os

def download_book(row):
    book = row["Book Title"]
    url = row["OpenURL"]
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()

    html = mybytes.decode("utf8")
    fp.close()

    start = html.find("/content/pdf/")
    substr = html[start:]
    end = substr.find(".pdf")
    book_name = book.replace(" ", "_").replace("/", "-") + ".pdf"

    path = "https://link.springer.com/" + substr[:end] + ".pdf"
    print(book)
    if os.path.isfile(book_name):
        print("File exist")
    else:
        wget.download(path, book_name)

#lista = str(sys.argv[1])
lista='lista.xlsx'
pandita = pd.read_excel('lista.xlsx')
print(pandita.head(2))

pandita.apply(download_book, axis=1)

