'''Convert number to string'''

# NUMBER TO Convert IN PYTHON (INDIAN SYSTEM) 
def Convert(n): 
    sat = ["Nol", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan"] # satuan
    las = ["Sepuluh","Sebelas"] # belas
    tus = ["Seratus"] # seratus
    # teens = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"] 
    # tens = ["Twenty","Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"] 
    if n <= 9:
        return sat[n]
    
    elif n == 10:
        return las[0]
    
    elif n == 11:
        return las[1]
    
    elif n == 100:
        return tus[0]
    
    elif n > 10 and n <= 19:
        return sat[n-10] + " Belas"
    
    elif n == 20 or n == 30 or n == 40 or n == 50 or n == 60 or n == 70 or n == 80 or n == 90:
        return sat[n // 10] + " Puluh"
    
    elif n >= 21 and n <= 99: # 20 // 10 = 2
        return sat[n // 10] + " Puluh " + (sat[n % 10] if n % 10 !=0 else "") # 20 % 10 = 0
    
    elif n >= 100 and n < 200:
        return tus[0] + " " + (Convert(n % 100) if n % 100 !=0 else "")
    
    elif n >= 200 and n <= 999:
        return Convert(n//100) + " Ratus " + (Convert(n % 100) if n % 100 !=0 else "")
    
satu = Convert(4)
belasan = Convert(12)
puluhan = Convert(735)
print(satu)
print(belasan)
print(puluhan)

# Code by Musfirotus