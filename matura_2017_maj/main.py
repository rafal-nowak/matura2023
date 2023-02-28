lines = [x.rstrip().split() for x in open("dane.txt", 'r').readlines()]

# 1
brightest = 0
darkest = 255
for i in range(len(lines)):
    for n in range(len(lines[i])):
        if int(lines[i][n]) > brightest:
            brightest = int(lines[i][n])
        if int(lines[i][n]) < darkest:
            darkest = int(lines[i][n])
print(f"Najjasniejszy piksel ma wartosc {brightest}, a najciemniejszy {darkest}")

# 2
counter = 0
for i in range(len(lines)):
    if lines[i] != lines[i][::-1]:
        counter+=1
print(counter)

# 3 (1 sposob)
counter = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if i == 0 and j == 0:
            if abs(int(lines[0][0]) - int(lines[1][0])) > 128:
                counter+= 1
            elif abs(int(lines[0][0]) - int(lines[0][1])) > 128:
                counter += 1
        if i == 0 and j == 319:
            if abs(int(lines[0][319]) - int(lines[0][318])) > 128:
                counter+= 1
            elif abs(int(lines[0][319]) - int(lines[1][319])) > 128:
                counter += 1
        if i == 199 and j == 0:
            if abs(int(lines[199][0]) - int(lines[199][1])) > 128:
                counter+= 1
            elif abs(int(lines[199][0]) - int(lines[198][0])) > 128:
                counter += 1
        if i == 0 and j == 0:
            if abs(int(lines[199][319]) - int(lines[199][318])) > 128:
                counter+= 1
            elif abs(int(lines[199][319]) - int(lines[198][319])) > 128:
                counter += 1
        if i == 0 and 0 < j < 319:
            if abs(int(lines[0][j]) - int(lines[0][j-1])) > 128:
                counter+= 1
            elif abs(int(lines[0][j]) - int(lines[0][j+1])) > 128:
                counter+= 1
            elif abs(int(lines[0][j]) - int(lines[1][j])) > 128:
                counter+= 1
        if i == 199 and 0 < j < 319:
            if abs(int(lines[199][j]) - int(lines[199][j-1])) > 128:
                counter+= 1
            elif abs(int(lines[199][j]) - int(lines[199][j+1])) > 128:
                counter+= 1
            elif abs(int(lines[199][j]) - int(lines[198][j])) > 128:
                counter+= 1
        if j == 0 and 0 < i < 199:
            if abs(int(lines[i][0]) - int(lines[i-1][0])) > 128:
                counter+= 1
            elif abs(int(lines[i][0]) - int(lines[i+1][0])) > 128:
                counter+= 1
            elif abs(int(lines[i][0]) - int(lines[i][1])) > 128:
                counter += 1
        if j == 319 and 0 < i < 199:
            if abs(int(lines[i][319]) - int(lines[i-1][319])) > 128:
                counter+= 1
            elif abs(int(lines[i][319]) - int(lines[i+1][319])) > 128:
                counter+= 1
            elif abs(int(lines[i][319]) - int(lines[i][318])) > 128:
                counter += 1
        if 0 < i < 199 and 0 < j < 319:
            if abs(int(lines[i][j]) - int(lines[i][j-1])) > 128:
                counter+= 1
            elif abs(int(lines[i][j]) - int(lines[i][j+1])) > 128:
                counter+= 1
            elif abs(int(lines[i][j]) - int(lines[i-1][j])) > 128:
                counter+= 1
            elif abs(int(lines[i][j]) - int(lines[i+1][j])) > 128:
                counter+= 1
print(counter)

# 3 (2 sposob)
counter = 0
for i in range(len(lines)):
    lines[i].insert(0, lines[i][0])
    lines[i].append(lines[i][-1])
lines.insert(0, lines[0])
lines.append(lines[-1])
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if 0 < i < 201 and 0 < j < 321:
                if abs(int(lines[i][j]) - int(lines[i][j-1])) > 128:
                    counter+= 1
                elif abs(int(lines[i][j]) - int(lines[i][j+1])) > 128:
                    counter+= 1
                elif abs(int(lines[i][j]) - int(lines[i-1][j])) > 128:
                    counter+= 1
                elif abs(int(lines[i][j]) - int(lines[i+1][j])) > 128:
                    counter+= 1
print(counter)

# 4
lines = [x.rstrip().split() for x in open("dane.txt", 'r').readlines()]
max_list = [0] * 320
list_length = [0] * 320
for i in range(len(lines)-1):
    for j in range(len(lines[i])):
        if int(lines[i][j]) == int(lines[i+1][j]):
            list_length[j] += 1
            if list_length[j] + 1 > max_list[j]:
                max_list[j] = list_length[j] + 1
        elif int(lines[i][j]) != int(lines[i+1][j]):
            if list_length[j] + 1 > max_list[j]:
                max_list[j] = list_length[j] + 1
            list_length[j] = 0
print(max(max_list))
