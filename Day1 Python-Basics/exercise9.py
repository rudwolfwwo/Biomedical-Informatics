import re

#a)
regex_number = re.compile("^-?[0-9]+(.?[0-9]+)?$")
print(re.fullmatch(regex_number,"Hallo"))#invalid
print(re.fullmatch(regex_number,"5"))
print(re.fullmatch(regex_number,"15.2343"))
print(re.fullmatch(regex_number,".3289"))#invalid
print(re.fullmatch(regex_number,"-324.4"))
print(re.fullmatch(regex_number,"3..3"))#invalid

#b)
d = "Man kann die Erkenntnisse der Medizin auf eine knappe Formel bringen: Wasser, mäßig genossen, ist unschädlich."
regex_len_three = "^[A-Za-z]{3}[^A-Za-z]|[^A-Za-z][A-Za-z]{3}[^A-Za-z]|[^A-Za-z][A-Za-z]{3}$"
print(re.findall(regex_len_three, d))
for word in re.finditer(regex_len_three, d):
    print(word.group(), "mit Anfangsindex:", d.find(word.group()))

#c)
regex_special_word = " [A-Z]{1}.{1,6} "
for word in re.finditer(regex_special_word, d):
    print(word.group())