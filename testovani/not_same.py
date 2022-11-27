a: int = 800
b: int = a * 1

print('a:', a)
print('b:', b)

print(a != b) # <- porovnává hodnoty
print(a is not b) # <- porovnává 'actual instance'

print('id(a):', id(a))
print('id(b):', id(b))