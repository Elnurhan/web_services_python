import requests
import re


result = requests.get("http://cbr.ru")
html = result.text

match = re.search(r"Евро\D+(\d+,\d+)", html)
rate = match.group(1)
print(rate)
