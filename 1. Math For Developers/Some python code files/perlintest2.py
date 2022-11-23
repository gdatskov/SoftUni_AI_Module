import noise
import numpy as np
import matplotlib.pyplot as plt

shape = (1024, 1024)
scale = 100.0
octaves = 6
persistence = 0.2
lacunarity = 2.0

world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i / scale,
                                    j / scale,
                                    octaves=octaves,
                                    persistence=persistence,
                                    lacunarity=lacunarity,
                                    repeatx=1024,
                                    repeaty=1024,
                                    base=0)

plt.imshow(world, cmap="gray")
plt.show()

blue = np.array([65,105,225])/255
green = np.array([34,139,34])/255
beach = np.array([238, 214, 175])/255

color_world = np.zeros(world.shape+(3,))
for i in range(shape[0]):
    for j in range(shape[1]):
        if world[i][j] < -0.05:
            color_world[i][j] = blue
        elif world[i][j] < 0:
            color_world[i][j] = beach
        elif world[i][j] < 1.0:
            color_world[i][j] = green


plt.imshow(color_world)
plt.show()
