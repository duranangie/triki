import datetime

# Funciones para el juego

def mostrar_tablero(tablero):

    for fila in tablero:

        print(" | ".join(fila))

        print("-" * 9)

def verificar_ganador(tablero, jugador):

  
    for i in range(3):

        if all([tablero[i][j] == jugador for j in range(3)]) or \
            all([tablero[j][i] == jugador for j in range(3)]):

            return True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador or \
        tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

def verificar_empate(tablero):

    return all(all(cell != " " for cell in fila) for fila in tablero)

def guardar_registro(jugador, puntaje, fecha):

    with open("registro.txt", "a") as archivo:

        archivo.write(f"{jugador}: {puntaje} puntos - {fecha}\n")

def reiniciar_juego():

  

    pass



def jugar_triki():

    jugador1 = input("Nombre del Jugador 1: ")

    jugador2 = input("Nombre del Jugador 2: ")

    puntaje_jugador1 = 0

    puntaje_jugador2 = 0

    while True:

        tablero = [

            [" ", " ", " "],

            [" ", " ", " "],

            [" ", " ", " "]

        ]

        turno = 1

        jugador_actual = jugador1

        while True:

          
            mostrar_tablero(tablero)

            fila = int(input(f"{jugador_actual}, elige una fila (0, 1, 2): "))

            columna = int(input(f"{jugador_actual}, elige una columna (0, 1, 2): "))

            

            if tablero[fila][columna] != " ":

                print("¡Casilla ocupada! Elige otra.")

                continue

           

            tablero[fila][columna] = "X" if jugador_actual == jugador1 else "O"

          

            if verificar_ganador(tablero, "X"):

                print(f"¡{jugador1} ha ganado!")

                puntaje_jugador1 += 1

                guardar_registro(jugador1, puntaje_jugador1, datetime.datetime.now())

                break

            elif verificar_ganador(tablero, "O"):

                print(f"¡{jugador2} ha ganado!")

                puntaje_jugador2 += 1

                guardar_registro(jugador2, puntaje_jugador2, datetime.datetime.now())

                break

            elif verificar_empate(tablero):

                print("¡Empate!")

                break

            
            jugador_actual = jugador2 if jugador_actual == jugador1 else jugador1

            turno += 1

if __name__ == "__main__":

    jugar_triki()