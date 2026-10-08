"""Simple 2D grid game prototype.
Move 'P' to reach 'G' in a 5x5 grid.
Use w/a/s/d keys, q to quit.
"""

def main():
    size = 5
    player = [0, 0]
    goal = [size - 1, size - 1]

    def draw():
        for y in range(size):
            row = ""
            for x in range(size):
                if [x, y] == player:
                    row += "P "
                elif [x, y] == goal:
                    row += "G "
                else:
                    row += ". "
            print(row.rstrip())
        print()

    moves = {'w': (0, -1), 'a': (-1, 0), 's': (0, 1), 'd': (1, 0)}
    while True:
        draw()
        if player == goal:
            print("Congratulations! You reached the goal.")
            break
        cmd = input("Move (w/a/s/d), q to quit: ").strip().lower()
        if cmd == 'q':
            print("Game terminated.")
            break
        if cmd in moves:
            dx, dy = moves[cmd]
            nx, ny = player[0] + dx, player[1] + dy
            if 0 <= nx < size and 0 <= ny < size:
                player = [nx, ny]
        else:
            print("Invalid command.\n")

if __name__ == "__main__":
    main()