import json

staffList = {'Company': [{'Address': '11223 Tran Hung Dao, District 1, HCM city',
                          'Phone': '08-83222145',
                          'ID': 1,
                          'Mail': 'hhsom2016@gmail.com',
                          'Min_Salary': 3500000,
                          'Name': 'Hoang Hon Som Co.,Ltd',
                          'Max_Age': 50,
                          'Min_Age': 20}],
             'Unit': [{'ID': 1,
                       'ID_Branch': 1,
                       'Staff_quantity': '14',
                       'Name': 'A1',
                       'Rate': '14.58'},
                      {'ID': 2,
                       'ID_Branch': 1,
                       'Staff_quantity': '15',
                       'Name': 'A2',
                       'Rate': '15.62'},
                      {'ID': 1,
                       'ID_Branch': 2,
                       'Staff_quantity': '14',
                       'Name': 'B1',
                       'Rate': '14.58'},
                      {'ID': 2,
                       'ID_Branch': 2,
                       'Staff_quantity': '20',
                       'Name': 'B2',
                       'Rate': '20.83'},
                      {'ID': 3,
                       'ID_Branch': 2,
                       'Staff_quantity': '19',
                       'Name': 'B3',
                       'Rate': '32.29'},
                      {'ID': 4,
                       'ID_Branch': 2,
                       'Staff_quantity': '14',
                       'Name': 'B4',
                       'Rate': '32.30'}]
             }
with open("Staff.json", "w", encoding="UTF-8") as f:
    json.dump(staffList, f, indent=4)
