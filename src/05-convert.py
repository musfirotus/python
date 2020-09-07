
'''Convert number to string'''

# referensi : https://pypi.org/project/num2words/

from num2words import num2words
# fromnya merah karena num2words butuh package 'wheel'

def Convert(num):
    # diconvert ke bahasa indo, terus tentukan formatnya
    return num2words(num, lang='id', to='cardinal') # sebenarnya defaultnya sudah cardinal

satu = Convert(1)
belasan = Convert(12)
puluhan = Convert(30)
print(satu)
print(belasan)
print(puluhan)

# Code by Musfirotus