# Un proyecto en español
# Gatito
import time
import os

# Función jugar de nuevo
def jugar_nuevo():
    jugar_gato = input("¿Quieres jugar de nuevo? ")
    while jugar_gato not in ["Sí", "Si", "sí", "si", "No", "no"]:
        jugar_gato = input("No entendi :(. ¿Quieres jugar de nuevo? ").lower()
    if jugar_gato.lower() == "sí" or "si":
        return True
    else:
        return False


# Displaying the board
def display(tablero):
    for renglon in tablero:
        print(renglon[0] + " | " + renglon[1] + " | " + renglon[2])
        print("---------")

# Winning combinations
def check_win(board):
    winning_combinations = [
        [[0, 0], [0, 1], [0, 2]],  # Top row
        [[1, 0], [1, 1], [1, 2]],  # Middle row
        [[2, 0], [2, 1], [2, 2]],  # Bottom row
        [[0, 0], [1, 0], [2, 0]],  # Left column
        [[0, 1], [1, 1], [2, 1]],  # Middle column
        [[0, 2], [1, 2], [2, 2]],  # Right column
        [[0, 0], [1, 1], [2, 2]],  # Diagonal from top-left to bottom-right
        [[0, 2], [1, 1], [2, 0]]   # Diagonal from top-right to bottom-left
    ]
    for combination in winning_combinations:
        marks = [board[pos[0]][pos[1]] for pos in combination]
        if len(set(marks)) == 1 and marks[0] != " ": #set counts how many elements are without repetitions
            return marks[0]    
    return None

#Getting the players' input
def get_player_move():
    while True:
        try:
            row = int(input("Enter the row number (0, 1, 2): "))
            col = int(input("Enter the column number (0, 1, 2): "))
            return row, col
        except ValueError:
            print("Invalid input. Please enter a valid row and column number.")

# Main
def gatito():
    limit = 9
    count = 0
    circles = "o"
    exes = "x"
    ocupado = []
    winner = None
    # Board
    tablero = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
        ]
    while winner is None:
        player1_sym = input(f"Jugador1 ¿Quién quieres ser hoy {circles} or {exes}\n").lower()
        if player1_sym not in ["x", "o"]:
            player1_sym = input(f"Lo siento, no entendí. Por favor elige entre {circles} y {exes}\n").lower()
        if player1_sym == circles: 
            player2_sym = exes
        else: player2_sym = circles
        print(f"Genial. Jugador 1: {player1_sym}. Jugador 2: {player2_sym}")
        while count < limit: 
            display(tablero)
            print("Jugador 1.\n")
            tiro1 = get_player_move()
            if tiro1 in ocupado:
                print("Oops, ocupado") 
                continue
            tablero[tiro1[0]][tiro1[1]] = player1_sym
            count = count + 1
            ocupado.append(tiro1)
            winner = check_win(tablero)
            if winner in [circles, exes]:
                display(tablero)
                print(f"Jugador {winner}. Has ganado!")
                return
            display(tablero)
            print("Jugador 2.\n")
            tiro2 = get_player_move()
            if tiro2 in ocupado:
                print("Oops, ocupado") 
                continue
            tablero[tiro2[0]][tiro2[1]] = player2_sym
            count = count + 1
            ocupado.append(tiro2)
            winner = check_win(tablero)
            if winner in [circles, exes]:
                display(tablero)
                print(f"Jugador {winner}. Has ganado!")
                return

# Start playing

def play_ttt():
    print("Hola! Bienvenidx al Juego del Gatito\n")
    print("   \o/  \n"
          "    |   \n"
          "   / \   \n")
    name1 = input("Jugador 1. Escribe tu nombre: ")
    name2 = input("Jugador 2. Escribe tu nombre: ")
    print(f"Hello {name1}, {name2}! Best of luck!")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    play = True
    while play:
        gatito()
        play = jugar_nuevo()
    print("Gracias por jugar! Bye!")
    print("   \o/  \n"
          "    |   \n"
          "   / \   \n")
    exit()

if __name__ == '__main__':
  play_ttt()