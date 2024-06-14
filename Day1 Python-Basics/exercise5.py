#a)
d = "Man kann die Erkenntnisse der Medizin auf eine knappe Formel bringen: Wasser, mäßig genossen, ist unschädlich."
dict = {}
for char in d.lower():
    dict[char] = d.lower().count(char)
print(dict)

#b)
print("Elemente, die häufiger als 5 mal vorkommen:")
for element in dict:
    if dict[element] > 5:
        print(element)

#c)
list = [element for element in dict]
list.sort()
string = ""
for e in list:
    if e != "e" and e != "i" and e != "n":
        string += ("'" + e + "'" + ":" + str(dict[e]) + ", ")
print(string, "\n")

#d)
set = {char for char in d}
l = [s for s in set]
l.sort()
for char in l:
    temp = "letter: '" + char + "' occurrence: "
    for i in range(0,len(d)):
        if d[i] == char:
            temp += str(i) + ", "
    print(temp)