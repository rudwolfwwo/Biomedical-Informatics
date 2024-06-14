#a)
a = 101
b = "3"
c = 0.25
d = "Man kann die Erkenntnisse der Medizin auf eine knappe Formel bringen: Wasser, mäßig genossen, ist unschädlich."
e = "(╯°□°）╯︵ ┻━┻"
ae_list = [a, b, c, d, e] #type is list which contains mixed types

#b)
pi_list = [3, 1, 4]

#c)
print(3 in ae_list) #false, because int 3 is not contained but the string '3'

#d)
string = "The sum of the lengths of the ae list (%i) and the pi list (%i) is %i" % (len(ae_list), len(pi_list), len(ae_list) + len(pi_list))

#e)
len_c = len(str(c))
len_d = len(d)
len_e = len(e)
print("sum of lengths of c,d and e: %i" % (len_c + len_d + len_e))

#f)
pi_list.extend(ae_list)
pi_list.reverse()
print(pi_list)

#g)
del pi_list[3]
print(pi_list)

#h)
d_list = d.split(" ")
print('-'.join(d_list))
