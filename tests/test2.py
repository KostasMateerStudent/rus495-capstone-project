import requests

r = requests.get("https://novayagazeta.ru/api/v1/search?q=%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F")

print(r.content)