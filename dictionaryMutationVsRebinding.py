def add_entry(d, key, value):
    d[key] = value 

def reassign_dict(d):
    d = {'x': 100}  


my_dict = {'a': 1}

add_entry(my_dict, 'b', 2)
print(my_dict)  

reassign_dict(my_dict)
print(my_dict)  