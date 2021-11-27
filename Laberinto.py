muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
laberinto = [[]] * 5

def construccion(fila, numero):
    if numero == 0:
        laberinto[0].append("X")
    if numero == 1:
        laberinto[1].append("X")
    if numero == 2:
        laberinto[2].append("X")
    if numero == 3:
        laberinto[3].append("X")
    if numero == 4:
        laberinto[4].append("X")

for i in range(5):
    for j in range(5):
        