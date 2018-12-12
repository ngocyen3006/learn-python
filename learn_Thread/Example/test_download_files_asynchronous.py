import threading
import requests
import time


class myThread(threading.Thread):
    def __init__(self, url, file_name):
        threading.Thread.__init__(self)
        self.url = url
        self.file_name = file_name

    def run(self):
        print("Start download " + self.url)
        Download_file(self.url, self.file_name)
        print("End download " + self.url)


def Download_file(url, file_name):
    r = requests.get(url)
    with open(file_name, "wb") as code:
        code.write(r.content)


threads = []
urls = ["https://www.iso.org/files/live/sites/isoorg/files/archive/pdf/en/annual_report_2009.pdf",
        "https://ars.els-cdn.com/content/image/1-s2.0-S0308814616314601-mmc1.pdf"]
file_names = ["annual_report_2009.pdf", "1-s2.0-S0308814616314601-mmc1.pdf"]
# Create new threads and Add threads to thread list
for url in urls:
    i = urls.index(url)
    threads.append(myThread(url, file_names[i]))
# Start new Threads
for t in threads:
    t.start()
start = time.time()
# Wait for all threads to complete
for t in threads:
    t.join()
elapsed = (time.time() - start)
print(elapsed, " seconds")  # 54.64558982849121  seconds
