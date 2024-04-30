import csv
import requests

base_url = "https://tomcat.pharmacyboardkenya.org/eac_rest_kentrade-1.0/"
payload = {"username": "",
           "password":""}

url = base_url + "login"
creds = requests.post(json=payload, url=url).json()
token = creds["access_token"]
headers = {"Accept": "application/json", "Authorization": "Bearer %s" % token}

# Products
datas = []
url_products = base_url + "products"
payload = {"start": 0, "limit": 10}
responses = requests.get(url_products, params=payload, headers=headers).json()
my_titles = responses["data"][0]
titles = []
for title in my_titles:
    titles.append(title)

for data in responses["data"]:
    for vals in data:
        dt = []
        for title in titles:
            dt.append(data[title])
    datas.append(dt)

with open('PPB_Products_List.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(titles)
    csvwriter.writerows(datas)

print(len(datas), 'Records Written to CSV')