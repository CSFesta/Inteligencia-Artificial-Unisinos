import random

def random_binary():
    return random.randrange(0,2)

def room_initialization(size, room):
    for i in range(size):
        for j in range(size):
            room[i][j] = random_binary()
    return room

def print_room(room):
    for row in room:
        for val in row:
            print(val, end=" ")
        print()


    

if __name__ == "__main__":
    size = int(input("Digite o tamanho da matriz:"))
    room = [[0 for _ in range(size)] for _ in range(size)]
    room = room_initialization(size, room)
    vis = [[False for _ in range(size)] for _ in range(size)]
    
    print_room(room)

    for i in range(size):
        for j in range(size):
            if(i%2==0):
                vis[i][j] = True
                if room[i][j] == 1:
                    print(f"Limpa na posição [{i}, {j}]")
                    room[i][j] = '#'
            else:
                vis[i][size - j - 1] = True
                if room[i][j] == 1:
                    print(f"Limpa na posição [{i}, {size - j - 1}]")
                    room[i][size - j- 1] = '#'
            
    print_room(room)

