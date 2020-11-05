my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [number for el, number in enumerate(my_list) if el > 0 and my_list[el] > my_list[el - 1]]
print(new_list)
