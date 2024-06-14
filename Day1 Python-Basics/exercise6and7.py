#6a)
def end_match(a, b):
    #7b)
    if type(a) is not str or type(b) is not str:
        raise TypeError("Übergeben werden sollen zwei Strings")

    return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())


#6b)
def alarm_clock(day, vacation):
    #7b)
    if type(day) is not int or type(vacation) is not bool:
        raise TypeError("Der Tag soll als int und vacation als bool übergeben werden")
    #7a)
    if day > 6 or day < 0:
        raise ValueError("Es gibt 7 Tage in der Woche")

    if day == 0 or day == 6:
        if vacation:
            return "off"
        else:
            return "10:00"
    else:
        if vacation:
            return "10:00"
        else:
            return "7:00"


#6c)
def date_fashion(you,date):
    #7b)
    if type(you) is not int or type(date) is not int:
        raise TypeError("Übergeben werden sollen zwei int Werte")
    #7a)
    if you < 0 or you > 10 or date < 0 or date > 10:
        raise ValueError("Die Range ist von 0 bis 10 definiert")

    if you > 8 or date > 8:
        return 2
    elif you < 3 or date < 3:
        return 0
    else:
        return 1


#6d)
def fibonacci(n):
    #7b)
    if type(n) != int: raise TypeError("Übergeben werden soll eine Ganzzahl")
    #7a)
    if n < 0: raise ValueError("Der übergebene Wert muss positiv sein")

    if n == 0: return 0
    elif n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(30)) #832040

#7c)
try:
    fibonacci(-1)
except:
    print("Success")

