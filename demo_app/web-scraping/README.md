# A Practical Introduction to Web Scraping in Python

## Scrape and Parse Text From Websites

```
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)

# returns the index of the first occurrence of a substring
title_index = html.find("<title>")
title_index


# extract the title by slicing the html string
start_index = title_index + len("<title>")
end_index = html.find("</title>")

title = html[start_index:end_index]
title

# extracting the title from new URL
url = "http://olympus.realpython.org/profiles/poseidon"

page = urlopen(url)
html = page.read().decode("utf-8")

start_index = html.find("<title >") + len("<title >")
end_index = html.find("</title>")

title = html[start_index:end_index]
title
```

## Get to Know Regular Expressions

```
import re

re.findall("as*d", "adasdasdasdasdasdad")
re.findall("ab*c", "ABC", re.IGNORECASE)

re.search("ab*c", "ABC", re.IGNORECASE).group()

string = "Everything is <replaced> if it's in <tags>."
re.sub("<replaced>", "ELEPHANTS", string)
re.sub("<.*>", "ELEPHANTS", string)
re.sub("<.*?>", "ELEPHANTS", string)
```

## Extract Text From HTML With Regular Expressions

```
import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)
```

## Use an HTML Parser for Web Scraping in Python

```
$ python -m pip install beautifulsoup4

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())
image1, image2 = soup.find_all("img")
image1["src"]

soup.title
soup.title.string
```

## Interact With HTML Forms

```
$ python -m pip install MechanicalSoup

import mechanicalsoup
browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"
page = browser.get(url)

type(page.soup)
page.soup
```

### Submit a Form With MechanicalSoup

```
import mechanicalsoup

# 1
browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

# 2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

# 3
profiles_page = browser.submit(form, login_page.url)

links = profiles_page.soup.select("a")
base_url = "http://olympus.realpython.org"
for link in links:
  address = base_url + link["href"]
  text = link.text
  print(f"{text}: {address}")
```

## Interact With Websites in Real Time

```
# mech_soup.py

import time
import mechanicalsoup

browser = mechanicalsoup.Browser()

for i in range(4):
  page = browser.get("http://olympus.realpython.org/dice")
  tag = page.soup.select("#result")[0]
  result = tag.text
  print(f"The result of your dice roll is: {result}")
  time.sleep(10)
```
