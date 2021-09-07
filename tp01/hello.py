# -*- coding: utf8 -*-

print("Hello")


# TheWorldIsFlat    => UpperCamelCase, PascalCase
# theWorldIsFlat    => camelCase
# the_world_is_flat => snake_case
# the-world-is-flat => kebab-case, train-case, spin-case

the_world_is_flat = True
c = 17 % 3
d = 17 ** 3

print(c)
print(d)


# Test si le monde est plat
if the_world_is_flat:
    print("Be careful not to fall off!")

s = "Bonjour"
s1 = 'Bonjour'
s2 = 'L\'orage gronde'
s3 = "L'orage gronde"
s4 = r"c:\newir\tir2"  # raw

s5 = """
        Le langage
        Python
        est
        beau
"""

s6_1 = "Python"
s6_2 = "est beau"
v = 3 # str(v) => 3 => "3"
str_v = str(v) # cast / transtypage

s7 = s6_1+str_v+" "+s6_2  # concaténation
print(s)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(50*'-')
print('-'*50)
print(s7)
# Python
# 012345
print(s6_1[0])
print(s6_1[2:4])
print(s6_1[2:])
print(s6_1[:2])




# print(s6_1)
# s6_1[0] = 'J'
# print(s6_1)
s6_1= "Jython"
print(s6_1)
# s6_1[0] = 'J'
s8 = s6_1[0]+"ython"
s9 = 'P'+s6_1[-len("toto"):]
print(s9)
s6_1 = 'L'+s6_1[1:]
print(s6_1)
print(len(s6_1+50*'-'))

squares = [1, 4, 9, 16, 25]
squares1 = squares[:]
print(squares)
print(squares1)
squares.append(36)

print(squares)
print(squares1)



a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


#   a,b = 1,  0+1 a=1 b=1
#   a,b = 1,  1+1 a=1 b=2
#   a,b = 2,  1+2 a=2 b=3