def add_two_numbers() -> int:
    user_input = input()
    string_split = user_input.split(",")
    x = string_split[0]
    y = string_split[1]
    return int(x) + int(y)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
