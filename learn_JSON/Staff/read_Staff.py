import json


def read_file_json(json_file):
    file = open(json_file, "r", encoding="UTF-8")
    data = json.load(file)
    file.close()
    return data


def read_company(data):
    for com in data:
        print(f"Company: {com['Name']}")
        print(f"Address: {com['Address']}")


def read_unit(data):
    Sum_Staff = 0
    stt = 0
    res = []
    for unit in data:
        stt += 1
        chuoi = f"{stt}. Name: {unit['Name']}" + '\n'
        chuoi += f" - Staff quantity: {unit['Staff_quantity']}" + '\n'
        chuoi += f" - Rate: {unit['Rate']} %"
        Sum_Staff += int(unit['Staff_quantity'])
        res.append(chuoi)
    result = [res, Sum_Staff]
    return result


if __name__ == '__main__':
    data = read_file_json("Staff.json")
    company = data['Company']
    read_company(company)
    unit = data['Unit']
    result = read_unit(unit)
    print(f"Staff quantity in company: {result[1]}")
    print("--------------------------------")
    for unit in result[0]:
        print(unit)
