with open('punkty.txt') as f:
    lines = f.read().splitlines()

# S = (a,b) -> a = 200 , b = 200

a = 200
b = 200
r = 200

counter = 0

for point in lines:
    # print(type(point))
    x, y = [int(x) for x in point.split()]

    if ((x - a) * (x - a) + (y - b) * (y - b) == r * r):
        print(f"Punkt na okregu: ({x},{y})")

    elif ((x - a) * (x - a) + (y - b) * (y - b) < r * r):
        counter += 1

print(counter)