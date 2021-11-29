muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
estructura = len(muro)
filasycolumnas = 5
#Se define con antelación el número de filas y columnas del laberinto
laberinto = [[]]
for p in range(filasycolumnas - 1):
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

for i in range(filasycolumnas):
    for j in range(filasycolumnas):
        comparacion(i, j)

laberinto[filasycolumnas - 1][len(laberinto[filasycolumnas - 1]) - 1] = "S"
for z in range(len(laberinto) - 1):
    print(str(laberinto[z]) +  ",")
print(laberinto[len(laberinto) - 1])