def LeapYear(years:int):
    if type(years) != int:
        raise ValueError
    elif (years % 4) == 0:
        if (years % 100) == 0:
            if (years % 400) == 0:
                print(type(years))
                return "Kabisat"
            else:
                return "Bukan Kabisat"
        else:
            return "Kabisat"
    elif years <= 0:
        return "Harus lebih dari nol!"
    else:
        return "Bukan Kabisat"

print(LeapYear(2000))