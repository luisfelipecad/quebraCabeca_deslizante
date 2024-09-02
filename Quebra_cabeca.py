from collections import deque

def move(matrix, direction):
    # Encontrar a posição do espaço vazio (0)
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                x, y = i, j

    # Mover o espaço vazio na direção especificada
    if direction == 'left' and y > 0:
        matrix[x][y], matrix[x][y-1] = matrix[x][y-1], matrix[x][y]
    elif direction == 'right' and y < 2:
        matrix[x][y], matrix[x][y+1] = matrix[x][y+1], matrix[x][y]
    elif direction == 'up' and x > 0:
        matrix[x][y], matrix[x-1][y] = matrix[x-1][y], matrix[x][y]
    elif direction == 'down' and x < 2:
        matrix[x][y], matrix[x+1][y] = matrix[x+1][y], matrix[x][y]
    
    return matrix

def is_solved(matrix):
    return matrix == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def solve_sliding_puzzle(initial_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, moves = queue.popleft()

        if is_solved(state):
            return moves

        for direction in ['left', 'right', 'up', 'down']:
            new_state = [row[:] for row in state]
            new_state = move(new_state, direction)
            state_tuple = tuple(map(tuple, new_state))
            if state_tuple not in visited:
                visited.add(state_tuple)
                queue.append((new_state, moves + [direction]))

    return None

def print_board(matrix):
    for row in matrix:
        print(' '.join(str(num) for num in row))
    print()

# Exemplo de uso
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 8]
]

print("Estado inicial:")
print_board(matrix)

solution = solve_sliding_puzzle(matrix)
if solution:
    print("\nSolução encontrada!")
    print("Movimentos necessários:")
    for move in solution:
        print(move)
else:
    print("\nNão foi possível encontrar uma solução.")




