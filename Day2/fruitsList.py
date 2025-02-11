thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
for item in thislist:
    print(item)

# Acessing List Items

# list indexing
print(thislist[0]) #1st item
print(thislist[1]) # 2nd item in list
print(thislist[-1]) # last item in list

# list slicing
print(thislist[2:5]) # 3rd to 5th item
print(thislist[:4]) # beginning to 3rd item
print(thislist[2:]) # 3rd to last item
print(thislist[1:5:2]) # 2nd to 5th item step size 2
print(thislist[::2]) # 1st to last item step size 2