import matplotlib.pyplot as plt
import numpy as np


class Fish():
    def __init__(self, size=20, speed=1, x=0, y=50, color='r'):
        self.size = size
        self.speed = speed
        self.x = x
        self.y = y
        self.color = color

fish = Fish()

plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()

while True:
    fish.x = fish.x + fish.speed
    fish.y = fish.y + fish.speed
    plt.scatter(fish.x, fish.y, color=fish.color, s=fish.size)
    plt.draw()

