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



# Number 3
text_1 = "Mammals".lower()
text_2 = "Bruiser build".lower()

def charcount(str):
    arr = {}
    for x in str:
        if x in arr:
            arr[x] += '*'
        elif x not in arr:
            arr[x] = '*'
    print(arr)

print(charcount(text_1))
print(charcount(text_2))



# Number 4
def bubble_sort(items) :
    x = 0
    for i in range(len(items)-1,0,-1):
        for j in range(i):
            if items[j]>items[j+1]:
                if(j>-1):
                    x += 1
                    print(f'Step {x} :', items)
                temp = items[j]
                items[j] = items[j+1]
                items[j+1] = temp
    
numbers = [12,3,5,4,8,9]
bubble_sort(numbers)



# Number 5
def masking(str):
    print('*' * len(str))

secret_text = "23dn3ir30fd2eddd"
masking(secret_text)



# Number 6
import string

list_letters_first = ["c","d","e","g","h"]
list_letters_second = ["X","Z"]

def missing_letter(chars):
    charset = string.ascii_lowercase if chars[0] >= 'a' else string.ascii_uppercase
    for letter in charset[charset.index(chars[0]):]:
        if letter not in chars:
            return letter[0]

print('list_letters_first =', missing_letter(list_letters_first))
print('list_letters_second =', missing_letter(list_letters_second))


# Number 7
def sort_odd(source_array):
    odd_numbers = sorted([n for n in source_array if n%2!=0])
    c = 0
    res = []
    for i in source_array:
        if i %2!=0:
            res.append(odd_numbers[c])
            c += 1
        else:
            res.append(i)
    print(res)
numbers = [9,4,2,4,1,5,3,0]
sort_odd(numbers)