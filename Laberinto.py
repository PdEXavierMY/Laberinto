muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
estructura = len(muro)
ultima_coordenada = muro[(estructura - 1)][0]
laberinto = [[]]
for p in range(ultima_coordenada):
    laberinto += [[]]

def comparacion(i, j):
    haymuro = False
    for k in range(estructura):
        if muro[k] == (i, j):
            laberinto[i].append("X")
            haymuro = True
            break
    if haymuro == False:
        laberinto[i].append(" ")
    return laberinto

for i in range(ultima_coordenada + 1):
    for j in range(ultima_coordenada + 1):
        comparacion(i, j)

laberinto[(len(laberinto) - 1)].pop()
laberinto[(len(laberinto) - 1)].append("S")
for z in range(len(laberinto) - 1):
    print(str(laberinto[z]) +  ",")
print(laberinto[len(laberinto) - 1])