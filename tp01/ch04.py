# s = input("Please enter an integer: ")  # str

# x = int(s)

# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0 or x == 2:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

l = ['value_1','value_2','value_3','value_4','value_5']

# for item in l[:]:
#     print(item,len(item))


print(list(range(5)))
# range(5)
for i in range(len(l)):
    print(i,l[i])

for i,v in enumerate(l):
    print(i,v)

c= [10,22,50,90]
print(sum(c))


if c[0]==2:
    pass

print("toto")

