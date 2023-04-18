with open('punkty.txt') as f:
    lines = f.read().splitlines()

# S = (a,b) -> a = 200 , b = 200

a = 200
b = 200
r = 200

n = 10000 #  z tresci
p = 400*400 # pole = bok * bok

# Pk = pi * r*r

# nk / n = pi * r*r / p
# p * nk / n * r*r = pi

nk = 0
n = 1000
for point in lines[:1000]:
    x, y = [float(x) for x in point.split()]
    if ( (x-a)*(x-a) + (y-b)*(y-b) <= r*r ):
        nk += 1

pi = (p * nk) / (n * r*r)
print(f"Dla 1000 punktow Pi wynosi {round(pi, 4)}")

nk = 0
n = 5000
for point in lines[:5000]:
    x, y = [float(x) for x in point.split()]
    if ( (x-a)*(x-a) + (y-b)*(y-b) <= r*r ):
        nk += 1

pi = (p * nk) / (n * r*r)
print(f"Dla 5000 punktow Pi wynosi {round(pi, 4)}")

nk = 0
n = 10000
for point in lines:
    x, y = [float(x) for x in point.split()]
    if ( (x-a)*(x-a) + (y-b)*(y-b) <= r*r ):
        nk += 1

pi = (p * nk) / (n * r*r)
print(f"Dla 10000 punktow Pi wynosi {round(pi, 4)}")