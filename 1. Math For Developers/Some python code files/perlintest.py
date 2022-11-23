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
