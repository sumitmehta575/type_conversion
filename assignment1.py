#1.Covert a integer to a floatig-point number.
a = 1
print(type(a))
b = float(a)
print(type(b))

#2.Covert a float to a integer.
s=2.0
print(type(s))
c=int(s)
print(type(c))

#3.Covert a integer to a string.
m=2
print(type(m))
d=str(s)
print(type(d))

#4.Covert a list to a tuple.
def convert (list):
    return tuple(list)
list=[1,2,3]
print(convert(list))

#5.Covert a tuple to a list.
atuple=(1,2,3)
alist=[*atuple]
print(alist)

#6.Covert a decimal number to binary.
r=3
e=bin(3)
print(e)

#7.Covert a non-zero number to boolean.
g=4
h=bool(1)
print(h)