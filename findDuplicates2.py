my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicatelist = []
for elem in my_list:
    if my_list.count(elem) > 1:
        if elem not in duplicatelist:
            duplicatelist.append(elem)
print(duplicatelist)


