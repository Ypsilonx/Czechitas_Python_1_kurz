my_list = ['a', 'b', 'd', 'e', 'f', 'g']
# print(my_list)

my_val = 'c'

# use .insert(index, item)
# my_list.insert(2, my_val)
# print(my_list)

# use slice notation list[index:index] = item
# my_list[2:2] = my_val
# print(my_list)

# my_list2 = ['a', 'b', 'd', 'e', 'f', 'g', 'c']
# print(my_list2)

# my_list2.insert(2, my_list2.pop(6))
# print(my_list2)

my_list3 = ['c', 'a', 'b', 'd', 'e', 'f', 'g']
print(my_list3)

my_list3.insert(2, my_list3.pop(0))
print(my_list3)