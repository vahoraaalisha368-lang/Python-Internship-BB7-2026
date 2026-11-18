def get_value(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        return None

my_list = ["alisha", "aaysha", "aris"]

print(get_value(my_list, 1)) 
print(get_value(my_list, 10)) 
print(get_value(my_list, 0))  