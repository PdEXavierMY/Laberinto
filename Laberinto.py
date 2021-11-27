muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
estructura = len(muro)
ultima_coordenada = muro[(estructura - 1)][0]
laberinto = [[]] * (ultima_coordenada + 1)

print(laberinto)

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

def caca():
        for i in range(ultima_coordenada + 1):
            for j in range(ultima_coordenada + 1):
                print(i, j)
                comparacion(i, j)

comparacion(0, 0)
print(laberinto)