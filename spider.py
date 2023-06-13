from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
#This tool works like some famous subdomain scanner such as
# AMASS, SubBrute, Knock, DNSRecon, Sublist3r, and more

#Output dari program ini adalah semua link dari href (dijoin dengan url dasar yg kita masukkan ke program) yang ada di
# halaman website/URL yang kita masukkan ke program, semua link tersebut tidak memiliki duplikat

listed_url = set()

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Some error occured when trying to requests.get this URL {url}")
        return
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        aTag = soup.find_all('a')
        #urls adalah list yang berisi link href dari halaman website atau URL yang kita masukkan
        urls = []
        for tag in aTag:
            href = tag.get('href')
            if href is not None and href != "":
                urls.append(href)

        #set listed_url berisi urls2 dari list urls yang sudah disortir agar tidak ada duplikat 
        for urls2 in urls:
            if urls2 not in listed_url:
                listed_url.add(urls2)
                URL_join = urljoin(url, urls2)
                if keyword in URL_join:
                    print(URL_join)
                    #spider_urls(URL_join, keyword)
                    #Di tutorial sebenarnya pakai call function spider_urls() tapi di program ini ku comment/nonaktifkan
                    # agar output link dari program ini tidak terlalu banyak, tidak membebani komputer, dan agar aku
                    # lebih paham bagaimana kode program ini bekerja
            else:
                pass

url = input("What is the URL of the sites you want to scrape? ")
keyword = input("What is the keyword for the provided URLs? ")
spider_urls(url, keyword)