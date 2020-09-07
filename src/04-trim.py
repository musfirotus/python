'''Trim characters/text'''

# referensi : https://stackoverflow.com/questions/2872512/python-truncate-a-long-string

# memanfaatkan logika range [a:b] dan ternary operator
def Trim(val = "", lim = 6, seperator = "..."):
    info = (val[:lim] + '..') if lim >= 2 else "Minimal limit 2"
    print(info)

Trim("ini adalah tulisan yang sangat panjang",7)

# Code by Musfirotus