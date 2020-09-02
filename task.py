# Number 1
first = ['Behind', 'every', 'great', 'man']
second = ['is', 'a', 'woman']
third = ['rolling', 'her', 'eyes']

def list_string(org_list, separator=' '):
    return separator.join(org_list)

print(list_string(first + second + third))