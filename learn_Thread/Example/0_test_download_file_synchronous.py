import requests

# xử lý đồng bộ (synchronous)
url = "https://www.iso.org/files/live/sites/isoorg/files/archive/pdf/en/annual_report_2009.pdf"
print("Start download")
r = requests.get(url)
with open("annual_report_2009.pdf", "wb") as code:  # mở tập tin cho phép ghi dữ liệu nhị phân
    code.write(r.content)
print("End download")
a = int(input("Số a = "))
b = int(input("Số b = "))
s = a + b
print("Tổng %i + %i = %i" % (a, b, s))
