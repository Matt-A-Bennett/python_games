import snake
import numpy as np

snake = snake.Snake(np.array([5,6,7]), np.array([5,5,5]))

alive = True
while alive:

    if is_food():
        snake.eat()
    elif is_obstacle():
        alive = False
    snake.update()

print('GAME OVER\n')
print(f'Score: {snake.get_length()}')
