import math
import matplotlib.pyplot as plt

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
n = 0
res_pi = []
res_e = []
for point in lines[:1700]:
    n += 1
    x, y = [float(x) for x in point.split()]

    if ( (x-a)*(x-a) + (y-b)*(y-b) <= r*r ):
        nk += 1

    pi = (p * nk) / (n * r*r)
    res_pi.append(pi)
    res_e.append(abs(math.pi - pi))


print(f'Wartosci dla e_1000 i e_1700: {round(res_e[999], 4)}, {round(res_e[1699], 4)}')

plt.plot(range(0,1700),res_e)
plt.title('Blad bezwzgledny')
plt.show()