'''Trim characters/text'''

# referensi : https://stackoverflow.com/questions/2872512/python-truncate-a-long-string

# memanfaatkan logika range [a:b] dan ternary operator
def Trim(val:str = "", lim:int = 2):
    if type(val) != str or type(lim) != int:
        raise ValueError
    else:
        return (' '.join(val.split(" ")[:lim])) if lim >= 1 else "Minimal limit 1"

Trim("ini adalah tulisan yang sangat panjang",1)

# Code by Musfirotus