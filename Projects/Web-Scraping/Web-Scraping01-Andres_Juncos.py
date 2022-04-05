# import webbrowser
# webbrowser.open("https://www.gutenberg.org/")
import requests
res = requests.get("https://www.gutenberg.org/cache/epub/67775/pg67775.txt")
print(len(res.text))
print(res.text[:300])