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



# Number 3 => belum bisa replace sesuai jumlah
from collections import Counter

text_1 = "Mammals".lower()
text_2 = "Bruiser build".lower()

def charcount(stri):
    return Counter(stri)

print(charcount(text_1))
print(charcount(text_2))



# Number 4 => step 6 kenapa jadi step 2??
def bubble_sort(items) :
    for i in range(len(items)-1,0,-1):
        for j in range(i):
            if items[j]>items[j+1]:
                print('Step ', j+1, ':', items)
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
    
numbers = [12,3,5,4,8,9]
bubble_sort(numbers)
# print(numbers)