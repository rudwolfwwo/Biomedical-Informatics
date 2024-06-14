#a) + b)
a = 101 #int
b = "3" #string
c = 0.25 #float
d = "Man kann die Erkenntnisse der Medizin auf eine knappe Formel bringen: Wasser, mäßig genossen, ist unschädlich." #string
e = "(╯°□°）╯︵ ┻━┻" #string

#c)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

#d)
f = (a + int(b)) #because a is int b has to be converted to int aswell (or both to string) -> f is int
g = ((a + int(b)) * (a + int(b))) / c #because of division with c is g a float -> g is float
print("f is %d and g is %f" % (g,f))
print("f has type ", type(f), " g has type ", type(g))

#e)
str = "%i modulo %i result into %i" % (a, int(b), a % int(b)) #str has value 2
print(str)

#f)
print(d + "\t" + e)