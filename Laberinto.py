muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
estructura = len(muro)
ultima_coordenada = muro[(estructura - 1)][0]
laberinto = [[]] * (ultima_coordenada + 1)

print(laberinto)

def construccion(i, j):
    for k in muro:
        if k == (i, j):
            laberinto[i].append("X")
        else:
            laberinto[i].append(" ")

for i in range(5):
    for j in range(5):
        construccion(i, j)

print(laberinto)
print(estructura)