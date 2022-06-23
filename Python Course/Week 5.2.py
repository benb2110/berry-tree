y = "Hello"
x = y
print(hex(id(y)))
print(hex(id(x)))
x.clear()
print(y)
