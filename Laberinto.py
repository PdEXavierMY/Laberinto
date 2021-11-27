muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
laberinto = [[]] * 5

def construccion(i, j):
    if muro[0] == (i, j):
        laberinto[i].append("X")
    elif muro[1] == (i, j):
        laberinto[i].append("X")
    elif muro[2] == (i, j):
        laberinto[i].append("X")
    elif muro[3] == (i, j):
        laberinto[i].append("X")
    elif muro[4] == (i, j):
        laberinto[i].append("X")
    else:
        laberinto[i].append(" ")

for i in range(5):
    for j in range(5):
        construccion(i, j)

print(laberinto)
