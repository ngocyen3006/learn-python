print("-------------------------------")
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

print("-------------------------------")
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))
print("-------------------------------")
print(astring.index("o")) #vi tri chu "o" dau tien "H" la vi tri 0
print("-------------------------------")
print(astring.count("l")) #dem chu "l"
print("-------------------------------")
print(astring[3:7]) # in ky tu tu vi tri 3 den 6
print("-------------------------------")
print(astring[3:7:2]) # tra ve vi tri 3 va 5 la l va khoang trang
print("-------------------------------")
print(astring[3:7:1]) # [start : stop : step], tra ve vi tri 3 4 5 6
print("-------------------------------")
print(astring[::-1]) # step = -1, tra vi tri nguoc
print("-------------------------------")
print(astring.upper()) # chuyen thanh chu hoa
print(astring.lower()) # chuyen thanh chu thuong
print("-------------------------------")
print(astring.startswith("Hello")) #xac dinh chuoi bat dau, ket qua tra ve True 
print(astring.endswith("asdfasdfasdf")) # xac dinh chuoi ket thuc, ket qua tra ve False
print("-------------------------------")
print("The last five characters are '%s'" % astring[-5:]) # 5th-from-last to end
print("-------------------------------")
afewwords = astring.split(" ")
print(afewwords)

