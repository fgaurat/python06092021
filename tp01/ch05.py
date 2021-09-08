from collections import deque

l = [10, 50, 90, 80, 70, 2]
q = deque(l)
print(l, len(l))
print(l.pop())  # != l[-1]
print(l, len(l))
q.appendleft(12)
print(l)
print(q)


# res = []
# # res = [20,100,180,160,140,4]


# for i in l:
#     res.append(i*2)
# print(res)


# def mult2(a):
#     return a*2


# res = list(map(mult2,l))
res = list(map(lambda d:d*2,l))
# print(res)

# print(hello_pos.__doc__)

squares = [x**2 for x in range(0, 10, 2)]

minus = ["toto", "tutu", "tata"]

majus = [m.upper() for m in minus if m != "toto"]


for m in minus:
    if m != "toto":
        majus.append(m.upper())

print(majus)


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print(matrix[1][2])


l1 = [1, 2, 3]
l2 = [4, 5, 6, 1007]
l3 = [14, 15, 16, 56, 97]
print(list(zip(l1, l2, l3)))

a = 0, 1
# a[0] = 12
print(a)


def f(*a):
    # a[0]=12
    print(a)


f(2, 3)

d = {'name': "toto", "fname": "tutu"}
for t in d.items():
    k, v = t  # 'name', 'toto'
    print(k)
    print(v)

t = 1,
print(t)

languages = {'java', 'python', 'perl', 'ruby', 'perl'}
# languages = set(['java','python','perl','ruby','perl'])
print(languages)
print('java' in languages)

if 'java' in languages:
    print("java ok")

tel = {'jack': [159, 987], 'sape': [4139]}
print(tel['jack'])
tel['jack'] = [159, 987]
print(tel['jack'])
print(tel['sape'][0])
# tel['toto'] = [5879]
print(tel)

if 'toto' in tel:
    tel['toto'].append(8978)
else:
    tel['toto'] = [8978,1234]

print(tel)
keys = list(tel.keys())
values = list(tel.values())
print(keys)
print(values)

for i in tel.keys():
    print(i)

# a = 'in' if 'toto' in tel else 'not in'
# print(a)


for k,v in tel.items():
    print(k,v)

l =[10,20,30]
for i,d in enumerate(l):
    print(i,d)

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = [value for value in raw_data if not math.isnan(value)]

# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)

print(filtered_data)