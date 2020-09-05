'''Querying and fetch data'''
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["age"])
import urllib.request, json 
with urllib.request.urlopen("https://mul14.github.io/data/employees.json") as url:
    data = json.loads(url.read().decode())
    # print(data)

def salary(val):
    return val['first_name'] if int(val['salary']) > 15000000 else False

def jakarta(val):
    return val['first_name'] if str(val['addresses'][0]['city']) == 'DKI Jakarta' else False

upSalary = filter(None, map(salary,data))
inJakarta = filter(None, map(jakarta,data))

print("Gaji diatas 15 JT :\n", ", ".join(list(upSalary)))
print("Alamat di DKI Jakarta :\n", ", ".join(list(inJakarta)))

# Code by Musfirotus