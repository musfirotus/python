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
    # if (int(val['salary']) > 15000000):
    #     return val['first_name']
    # else:
    #     return

upSalary = filter(None, map(salary,data))
print(",".join(list(upSalary)))