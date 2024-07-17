import requests
import time

def measure_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    load_time = end_time - start_time
    return load_time

sites = ["https://www.google.com", "https://www.ynet.co.il",
         "https://yad2.co.il", "https://youtube.com",
         "https://www.imdb.com"]

for site in sites:
    load_time = measure_load_time(site)
    print(f"The load time for {site} is {load_time:.2f} seconds")
