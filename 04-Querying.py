'''Querying and fetch data'''

import urllib.request, json 
with urllib.request.urlopen("https://mul14.github.io/data/employees.json") as url:
    data = json.loads(url.read().decode())
    # print(data)

def salary(val):
    return val['first_name'] if int(val['salary']) > 15000000 else "Data tidak ada!"

def jakarta(val):
    # ['addresses'][0]['city'] mengambil object didalam array
    return val['first_name'] if str(val['addresses'][0]['city']) == 'DKI Jakarta' else "Data tidak ada!"

def month(val):
    return val['first_name'] if str(val['birthday'].split('-')[1]) == '04' else "Data tidak ada!"

def dept(val):
    # ['department']['name'] langsung mengambil object
    return val['first_name'] if str(val['department']['name']) == 'Research and development' else "Data tidak ada!"

def absence(val):
    return val['first_name'] if str(val['presence_list'].split('-')[0:1000]) == '10' else "Data tidak ada!"

upSalary = filter(None, map(salary,data))
inJakarta = filter(None, map(jakarta,data))
month = filter(None, map(month,data))
inDept = filter(None, map(dept,data))
inAbsence = filter(None, map(absence,data))

print("Gaji diatas 15 JT :\n", ", ".join(list(upSalary)))
print("Alamat di DKI Jakarta :\n", ", ".join(list(inJakarta)))
print("Lahir di bulan April :\n", ", ".join(list(month)))
print("Di departement Research :\n", ", ".join(list(inDept)))
print("Yg Absen di bln Oktober :\n", ", ".join(list(inAbsence)))

# Code by Musfirotus