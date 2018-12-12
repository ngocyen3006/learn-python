import threading
import requests
import time


# xử lý bất đồng bộ (asynchronous)


class myThread(threading.Thread):
    def __init__(self, url, file_name):
        threading.Thread.__init__(self)
        self.url = url
        self.file_name = file_name

    def run(self):
        print("Start download")
        Download_file(self.url, self.file_name)
        print("End download")


def Download_file(url, file_name):
    start = time.time()
    r = requests.get(url)
    with open(file_name, "wb") as code:
        code.write(r.content)
    elapsed = (time.time() - start)
    print(elapsed, " seconds")  # 50.998727321624756  seconds


url = "https://www.iso.org/files/live/sites/isoorg/files/archive/pdf/en/annual_report_2009.pdf"
file_name = "annual_report_2009.pdf"
# Create new threads
thread = myThread(url, file_name)
# Start new Threads
thread.start()
# Continue main thread
a = int(input("Số a = "))
b = int(input("Số b = "))
s = a + b
print("Tổng %i + %i = %i" % (a, b, s))
# Wait for all threads to complete
thread.join()
