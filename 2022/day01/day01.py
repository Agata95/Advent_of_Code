
with open('day01.txt', 'r') as file:
    numbers_list = file.readlines()

############################################
# Part 1

all_list = []
calory_list = []

for el in numbers_list:

    if el != '\n':
        calory_list.append(int(el))
    else:
        all_list.append(sum(calory_list))
        calory_list = []

# print(max(all_list))


############################################
# Part 2

max_1 = max(all_list)
all_list.remove(max_1)
max_2 = max(all_list)
all_list.remove(max_2)
max_3 = max(all_list)

print(max_1, max_2, max_3)
print(sum([max_1, max_2, max_3]))