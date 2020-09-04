'''Trim characters/text'''

def Trim(val = "", lim = 6, seperator = "..."):
    info = (val[:lim] + '..') if lim >= 2 else "Minimal limit 2"
    print(info)

Trim("ini adalah tulisan yang sangat panjang",7)