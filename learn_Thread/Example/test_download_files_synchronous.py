import requests
import time


def Download_files(urls, file_names):
    start = time.time()
    for i in range(len(urls)):
        url = urls[i]
        print("Start download: " + url)
        r = requests.get(url)
        file_name = file_names[i]
        with open(file_name, "wb") as code:
            code.write(r.content)
        print("End download: " + url)
    elapsed = (time.time() - start)
    print(elapsed, " seconds")  # 94.20911502838135  seconds


urls = ["https://www.iso.org/files/live/sites/isoorg/files/archive/pdf/en/annual_report_2009.pdf",
        "https://ars.els-cdn.com/content/image/1-s2.0-S0308814616314601-mmc1.pdf"]
file_names = ["annual_report_2009.pdf", "1-s2.0-S0308814616314601-mmc1.pdf"]

Download_files(urls, file_names)
