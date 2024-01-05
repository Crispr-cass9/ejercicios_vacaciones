from random import randrange

    
board = [[1,2,3]
       ,[4,'X',6]
       ,[7,8,9]]

jugadas_totales=0

fila_movimiento = None
columna_movimiento = None
empate=False
def DisplayBoard(board):

    print('+-------+-------+-------+\n',
      '|       |       |       |\n',
      '|   ', board[0][0],'   |   ',board[0][1],'   |   ',board[0][2],'   |\n',
      '|       |       |       |\n',
      '+-------+-------+-------+\n',
      '|       |       |       |\n',
      '|   ', board[1][0],'   |   ',board[1][1],'   |   ',board[1][2],'   |\n',
      '|       |       |       |\n',
      '+-------+-------+-------+\n',
      '|       |       |       |\n',
      '|   ', board[2][0],'   |   ',board[2][1],'   |   ',board[2][2],'   |\n',
      '|       |       |       |\n',
      '+-------+-------+-------+\n',sep="")
    global jugadas_totales
    global empate
    jugadas_totales+=1
    print(jugadas_totales)
    if jugadas_totales == 9:
        empate=True
    return empate
    print('jugadas:', jugadas_totales)
    
def EnterMove(board):
    valida = False
    global fila_movimiento, columna_movimiento
    try:
        while not valida:
            jugada = int(input("Ingrese el número de su jugada: "))
            fila = (jugada-1)//3
            columna = (jugada-1)%3
                
            if not (board[fila][columna] == 'X' or board[fila][columna] == 'O'):
                board[fila][columna] = 'O'
                fila_movimiento = fila
                columna_movimiento = columna
                valida = True
            else:
                print('La jugada no es válida, esa posición ya se encuentra ocupada')
                valida = False
                
    except:
        print('No ha ingresado un valor válido')


def MakeListOfFreeFields(board):
    posiciones_vacias = []
    
    for elemento in board[0]:
        if type(elemento) == int:
            posiciones_vacias.append((0, (elemento-1)%3))
                                      
    for elemento in board[1]:
        if type(elemento) == int:
            posiciones_vacias.append((1, (elemento-1)%3))
                                      
    for elemento in board[2]:
        if type(elemento) == int:
            posiciones_vacias.append((2, (elemento-1)%3))
    
    return posiciones_vacias


def DrawMove(posiciones_vacias):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    print('Turno de la máquina')
    estado_columna = [board[fila][columna_movimiento] for fila in range(3)]

    if board[fila_movimiento].count('O') == 2 and fila_movimiento!=1 and board[fila_movimiento].count('X') == 0:
        board[fila_movimiento] = ['X' if signo != 'O' else 'O' for signo in board[fila_movimiento]]
    
    elif estado_columna.count('O') == 2 and columna_movimiento!=1 and estado_columna.count('X') == 0:
        for i in range(3):
            if board[i][columna_movimiento] != 'O':
                board[i][columna_movimiento] = 'X'
    else:
        jugada = posiciones_vacias[randrange(len(posiciones_vacias))]
        board[jugada[0]][jugada[1]] = 'X'

    

def VictoryFor(board, signo):
    global jugadas_totales
    if jugadas_totales >= 5:
        if board[0].count(signo) == 3:
            return True
        elif board[1].count(signo) == 3:
            return True
        elif board[2].count(signo) == 3:
            return True
        elif (board[0][0] == signo) and (board[1][0] == signo) and (board[2][0] == signo):
            return True
        elif (board[0][1] == signo) and (board[1][1] == signo) and (board[2][1] == signo):
            return True
        elif (board[0][2] == signo) and (board[1][2] == signo) and (board[2][2] == signo):
            return True
        if signo == 'X':
            if (board[0][0] == signo) and (board[2][2] == signo):
                return True
            if (board[2][0] == signo) and (board[0][2] == signo):
                return True
            
DisplayBoard(board)  

for i in range(8):
    EnterMove(board)
    DisplayBoard(board)
    if VictoryFor(board, 'O'):
        print("La victoria es para el humano")
        break
    if empate:
        print('Es un empate')
        break
    posiciones_vacias = MakeListOfFreeFields(board)
    DrawMove(posiciones_vacias)
    DisplayBoard(board)
    if VictoryFor(board, 'X'):
        DisplayBoard(board)
        print("La victoria es para la máquina")
        break
    if empate:
        print('Es un empate')
        break