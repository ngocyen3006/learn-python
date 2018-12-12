import _thread
import requests
import time

# xử lý bất đồng bộ (asynchronous)
da_xong = False


def Download_file(url, file_name):
    global da_xong
    start = time.time()
    da_xong = False
    r = requests.get(url)
    with open(file_name, "wb") as code:
        code.write(r.content)
    print("End download")
    elapsed = (time.time() - start)
    print(elapsed, " seconds")  # 70.05592751502991  seconds
    da_xong = True


print("Start download")
url = "https://www.iso.org/files/live/sites/isoorg/files/archive/pdf/en/annual_report_2009.pdf"
file_name = "annual_report_2009.pdf"
_thread.start_new_thread(Download_file, (url, file_name))

a = int(input("Số a = "))
b = int(input("Số b = "))
s = a + b
print("Tổng %i + %i = %i" % (a, b, s))
while not da_xong:
    pass
