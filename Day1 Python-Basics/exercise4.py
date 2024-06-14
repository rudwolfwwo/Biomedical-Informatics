#a)
result = 0
for i in range(1,251):
    result += i/(i + 1)
print(result)

#b)
d = "Man kann die Erkenntnisse der Medizin auf eine knappe Formel bringen: Wasser, mäßig genossen, ist unschädlich."
print("the characters 'e' and 'n' have the frequency: ", d.lower().count("e") + d.lower().count("n"))

#c)
s = ""
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        s += str(i) + ", "
print(s)

#d)
def matrix_generator(x,y):
    matrix = []
    for i in range(0, x):
        temp = [j * i for j in range(0, y)]
        matrix.append(temp)
    return matrix


print(matrix_generator(2, 2))
print(matrix_generator(3, 5))

