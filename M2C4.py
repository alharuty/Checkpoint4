import math

# EXERCISE 1

my_list = ["Maria", "John", "Carmen"]

my_tuple = ('a', 'b', 'c')

my_float = 3.33

my_integer = 42

my_decimal = 3.32

my_dictionary_users = {
    "John" : 28, 
    "Carl" : 29,
    "Erik" : 30,
}

# EXERCISE 2

my_up_float = math.ceil(my_float)
print(my_up_float)


# EXERCISE 3

my_sqrt = (math.sqrt(my_float))
print(my_sqrt)

# EXERCISE 4

first_element = list(my_dictionary_users.items())[0]
print(first_element)

# EXERCISE 5

second_element = my_tuple[1]
print(second_element)

# EXERCISE 6

my_list.append('Carolina')
print(my_list)

# EXERCISE 7

my_list[0] = 'Elena'
print(my_list)

# EXERCISE 8 

my_list.sort()
print(my_list)

# EXERCISE 9

my_tuple = my_tuple + ('d',)
print(my_tuple)