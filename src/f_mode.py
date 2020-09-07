'''Mode to show Frequent number'''

# Referensi : https://www.tutorialspoint.com/find-most-frequent-element-in-a-list-in-python

def Mode(val):
    if type(val) != list:
        raise ValueError
    else:
    # setnya nyari unique element, terus di count, terus kan ketemu element yg lengthnya paling besar.
        result = max(set(val), key = val.count)
        return result

numbers = [1,2,3,4,5,6,6,8,8,6,9]
grades = [87.5, 88.5, 60.5, 90.5, 88.5]

print(Mode(numbers))
print(Mode(grades))

# Code by Musfirotus