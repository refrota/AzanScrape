from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# downloads html file from KHEU web
my_url = 'http://www.kheu.gov.bn/Theme/Home.aspx'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# parse raw html file in soup
page_soup = soup(page_html, "html.parser")

# grabs prayer times
class_all = page_soup.findAll("td", {"class": "ms-vb"})
solat_times = class_all[3: 27]

imsak = solat_times[1].text
zohor = solat_times[4].text
subuh = solat_times[7].text
asar = solat_times[10].text
syuruk = solat_times[13].text
maghrib = solat_times[16].text
isya = solat_times[19].text

# grabs date (still on the works, unable to extract test)
# E_date = page_soup.findAll("div", {"id":"E_date"})
# print(E_date)

#print prayer times

print("=" * 40)
print()
print("Waktu solat pada hari ini adalah: ")
print()
print("Imsak: {} pagi".format(imsak))
print("Subuh: {} pagi".format(subuh))
print("Zohor: {} petang".format(zohor))
print("Asar: {} petang".format(asar))
print("Syuruk: {} petang".format(syuruk))
print("Maghrib: {} malam".format(maghrib))
print("Isya: {} malam".format(isya))
print()
print("=" * 40)
