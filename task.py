# Number 1
first = ['Behind', 'every', 'great', 'man']
second = ['is', 'a', 'woman']
third = ['rolling', 'her', 'eyes']

def list_string(org_list, separator=' '):
    return separator.join(org_list)

print(list_string(first + second + third))



# Number 2
menus = ["chicken strip", "beef burger", "steakhouse", "mushroom swiss", "whopper"] # List A
price = [15,10,12,20,30] # List B

res = {menus[i]: price[i] for i in range(len(menus))}

sorted_dict = dict(sorted(res.items(), key=lambda item: item[1], reverse=False))
print (sorted_dict)