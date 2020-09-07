  
'''Mode to show Frequent number'''

# Referensi : https://www.tutorialspoint.com/find-most-frequent-element-in-a-list-in-python
def Mode(val):
    # setnya nyari unique element, terus di count, terus kan ketemu element yg lengthnya paling besar.
    result = max(set(val), key = val.count)
    print("Element with highest frequency:\n",result)

numbers = [1,2,3,4,5,6,6,8,8,6,9]
grades = [87.5, 88.5, 60.5, 90.5, 88.5]

Mode(numbers)
Mode(grades)

# Code by Musfirotus