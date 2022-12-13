# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# score:
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

with open('day02.txt', 'r') as file:
    elements_list = file.readlines()

temp = [line[:-1] for line in elements_list]

score = 0

############################################
# Part 1

for el in temp:
    if el[0] == 'A':
        if el[2] == 'X':
            score += 4

        elif el[2] == 'Y':
            score += 8

        elif el[2] == 'Z':
            score += 3

    if el[0] == 'B':
        if el[2] == 'X':
            score += 1

        elif el[2] == 'Y':
            score += 5

        elif el[2] == 'Z':
            score += 9

    if el[0] == 'C':
        if el[2] == 'X':
            score += 7

        elif el[2] == 'Y':
            score += 2

        elif el[2] == 'Z':
            score += 6

# print(score)

############################################
# Part 2
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
# A for Rock, B for Paper, and C for Scissors
# score:
# 1 for Rock, 2 for Paper, and 3 for Scissors

score = 0

for el in temp:
    if el[0] == 'A':
        if el[2] == 'X':
            score += 3

        elif el[2] == 'Y':
            score += 4

        elif el[2] == 'Z':
            score += 8

    if el[0] == 'B':
        if el[2] == 'X':
            score += 1

        elif el[2] == 'Y':
            score += 5

        elif el[2] == 'Z':
            score += 9

    if el[0] == 'C':
        if el[2] == 'X':
            score += 2

        elif el[2] == 'Y':
            score += 6

        elif el[2] == 'Z':
            score += 7

print(score)