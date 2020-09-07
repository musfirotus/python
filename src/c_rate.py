# Jika usia yang dimasukkan lebih atau sama dengan 21, maka rating film adalah DEWASA.
# Jika usia yang dimasukkan lebih atau sama dengan 13, maka rating film adalah REMAJA.
# Jika usia yang dimasukkan lebih atau sama dengan 9, maka rating film adalah BIMBINGAN ORANG TUA.
# Jika usia yang dimasukkan kurang dari 9, maka rating film adalah SEMUA USIA.
# Contoh:
# Input: 15
# Output: Remaja

# Input: 32
# Output: Dewasa
def Rate(age):
    if type(age) != int or age < 0:
        raise ValueError
    elif age >= 21:
        return "DEWASA"
    elif age >= 13:
        return "REMAJA"
    elif age >= 9:
        return "BIMBINGAN ORANG TUA"
    elif age < 9 and age >= 0:
        return "SEMUA USIA"
    else:
        return "Masukkan usia yang VALID!"
    
print(Rate(23))
print(Rate(13))
print(Rate(10))
print(Rate(5))
print(Rate(3))