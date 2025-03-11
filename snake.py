'''
The snake’s initial size is 3
and grows by 1 every 5 moves, direction is right, left, up or down.
Snake initial = 3
when snake hit itself
when snake hit the wall
interface SnakeGame {

    moveSnake(snakeDirection);

    isGameOver();

'''


class SnakeGame:
    def __init__(self, grid=10):
        self.grid = grid
        self.snake = [(grid // 2, grid // 2 - i) for i in range(3)]
        self.direction = 'right'
        self.count = 0
        self.finish = False

    def moveSnake(self, snakeDirection):
        if self.finish:
            return "Game Over!"

        directions = {
            'up': (0, -1),
            'down': (0, 1),
            'left': (-1, 0),
            'right': (1, 0)
        }

        if snakeDirection not in directions:
            return "invalid direction"

        self.direction = snakeDirection

        head_x, head_y = self.snake[0]
        move_x, move_y = directions[self.direction]

        new_head = (head_x + move_x, head_y + move_y)

        if (new_head[0] < 0 or new_head[0] >= self.grid
                or new_head[1] < 0 or new_head[1] >= self.grid
                or new_head in self.snake):
            self.finish = True

        self.snake.insert(0, new_head)
        self.count += 1

        if self.count % 5 != 0:
            self.snake.pop()

        return self.count

    def isGameOver(self):
        return self.finish


moves = [
    "right", 'left', 'left', 'right',
    # "right", 'left', 'right', 'up',
    # "right", 'left', 'right', 'up',
    # "right", 'left', 'right', 'up',
    # "right", 'left', 'right', 'up',
    # "right", 'left', 'right', 'up',
]
results = []
snakeGame = SnakeGame()
for move in moves:
    result = snakeGame.moveSnake(move)
    results.append(result)

print(results)
