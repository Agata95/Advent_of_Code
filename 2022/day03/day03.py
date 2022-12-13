import copy

with open('day03.txt', 'r') as file:
    elements_list = file.readlines()

temp = [line[:-1] for line in elements_list]

############################################
# Part 1

result_all = []

for el in temp:
    result = []
    i = int(len(el) / 2)
    el_1 = el[:i]
    el_2 = el[i:]

    for e in el_1:
        for a in el_2:
            if e == a:
                result.append(e)
                result = list(dict.fromkeys(result))

    result_all.append(result[0])

result_2 = []

for el in result_all:
    if el.islower():
        result_2.append(ord(el) - 96)
    else:
        el_2 = el.lower()
        new = ord(el_2) - 70
        result_2.append(new)

# print(sum(result_2))


############################################
# Part 2

temp_list = copy.deepcopy(temp)
print(temp_list)
result_all = []
result_group = []

while len(temp_list) >= 3:
    result = []
    for e1 in temp_list[0]:
        for e2 in temp_list[1]:
            for e3 in temp_list[2]:
                if e1 == e2 and e2 == e3:
                    result.append(e1)
                    result = list(dict.fromkeys(result))
    result_group.append(result[0])
    for i in range(0, 3):
        temp_list.remove(temp_list[0])

print(result_group)
result_2 = []

for el in result_group:
    if el.islower():
        result_2.append(ord(el) - 96)
    else:
        el_2 = el.lower()
        new = ord(el_2) - 70
        result_2.append(new)
        print(el, new)

print(sum(result_2))
