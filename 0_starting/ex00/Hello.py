ft_list = ["Hello", "tata!"]  # list are mutable and ordered
ft_tuple = ("Hello", "toto!")  # tuple are immutable and ordered
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}  # dict are mutable and unordered key-value pairs

ft_list[1] = "World!"
ft_tuple = ("Hello", "France!")
ft_set = {"Hello", "Paris!"}
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)  # the print is unordered because set are unordered for print
print(ft_dict)
