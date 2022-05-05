import random

menu="\n“Battleship”\n\n1-Start\n2-Search\n3-Play\n4-Exit"

player_ships=[]
pc_ships=[]

BOATS=5

def initialize_pc_ships():
    global pc_ships
    
    pc_ships=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    i=1
    while i <= BOATS:
        pc_ships[random.randint(1,20)] = i
        i += 1
        
    return

def initialize_player_ships():
    global player_ships
    
    spot=0
    player_ships=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    i=1
    while i <= BOATS:
        print("\n")
        print(player_ships)
        spot=input("\nPlace Boat: ")
        player_ships[int(spot)-1] = i
        i += 1
    
    print(player_ships)
        
    return

def print_ships():
    print("\npc_ships: ")
    print(pc_ships)
    print("\nplayer_ships: ")
    print(player_ships)
    
    return 

def make_shoot(list, index):
    if list[int(index)-1] == 0:
        return -1
    elif list[int(index)-1] > 0:
        defeat = list[int(index)-1]
        list[int(index)-1] = 0
        return defeat
    
    return 

def print_winner(defeat_player, defeat_pc):
    if (defeat_jugador == defeat_pc):
        print("DRAW")
    elif (defeat_player > defeat_pc):
        print("Player WIN!")
    elif (defeat_player < defeat_pc):
        print("Computer WIN!") 
    return

while (True):
    print(menu)
    opcion=int(input(""))

    # START: En la opción 1 se deben usar las rutinas para inicializar los barcos de la computadora y del jugador.
    if opc == 1:
        initialize_pc_ships()
        initialize_player_ships()
        
    # SEARCH: En la opción 2 se debe usar la rutina para imprimir los barcos de la computadora y del jugador.
    elif opc == 2:
        print_ships()

    # PLAY: En la opción 3 se debe simular el juego entre el jugador y la computadora hasta que se llegue a 10 intentos o hasta que uno de los dos gane el juego. En la opción 3 se debe usar la rutina de hacer disparo y al final del juego la de imprimir ganador.
    elif opc == 3:
        defeat_player=0
        defeat_pc=0

        tries = 1
        while tries < 10 and defeat_player < 5 and defeat_pc < 5:
            print_ships()

            # PLAYER ATTACK
            if (make_shoot(pc_ships, input("\nAttack: ")) > 0):
                defeat_player += 1
            # COMPUTER ATTACK
            if (make_shoot(player_ships, random.randint(1, 20)) > 0):
                defeat_pc += 1
            
            tries += 1
        
        print_winner(defeat_player, defeat_pc)
            
    elif opc == 4:
        exit()
    else: 
        print("Invalid Option!")
