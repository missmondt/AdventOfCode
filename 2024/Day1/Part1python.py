# %%
#read file and strip /n
input = open('input.txt', 'r')
lines = input.readlines()
lines_stripped = [line.strip() for line in lines]

# %%
#split lines into list of lists and convert to dictionary
list_splitted = []
for line in lines_stripped:
    split_line = line.split()
    list_splitted.append(split_line)

dict1 = dict(list_splitted)

# %%
#divide dictionary into two lists
list1 = dict1.keys()
list2 = dict1.values()

# %%
#sort both lists
list1_sorted = sorted(list1)
list2_sorted = sorted(list2)

# %%
#calculate absolute differences between corresponding elements in the two lists
difflist = []
diff = 0
num = 0
for i in list1_sorted:
    j = list2_sorted[num]
    diff = int(j) - int(i)
    difflist.append(abs(diff))
    num = num + 1

# %%
#sum the differences
total = 0
for i in difflist:
    total = i + total
total


