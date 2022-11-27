
var: str = 'Banana'

# print(var) #<- Banana
# print(*var) #<- B a n a n a
# print(*var, sep='.') #<- B.a.n.a.n.a

list_: list[str] = [*var]

# print(list_) #<- ['B', 'a', 'n', 'a', 'n', 'a']

args: tuple = (1, 'a')

# print(args) #<- (1, 'a')
# print(*args) #<- 1 a

def func(a, b):
    print(a, b)

# func(*args) #<- 1 a