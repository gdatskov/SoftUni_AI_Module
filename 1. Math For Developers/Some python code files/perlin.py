import random
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt

noise = PerlinNoise(octaves=10, seed=random.randrange(1,1000000000000000))
xpix, ypix = 100, 100
pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

plt.imshow(pic, cmap='gray')
plt.show()