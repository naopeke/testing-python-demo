a = []
b = a
c = []

print(id(a))
print(id(b))
print(id(c))

a.append(35)
print(a)
print(b)
print(c)
print(id(a))
print(id(b))
print(id(c))

d = 8597
e = 8597

print(id(d))
print(id(e))