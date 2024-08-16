import beautifulsoup4 as bs4
import pandas as pd
import requests

source=requests.get("https://www.imdb.com/chart/top/")
print(source.content)