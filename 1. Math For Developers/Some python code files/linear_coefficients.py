import numpy as np
import matplotlib.pyplot as plt
from math import ceil


def plot_vectors(vectors, colors):
    """
    Plots vectors on the xy-plane. The `vectors` parameter is a Python list.
    Each vector is specified in the format [start_x, start_y, end_x, end_y]
    """
    info = zip(vectors, colors)

    x_vals = []
    y_vals = []

    for vec, colr in info:
        x_0, y_0, x, y = vec
        x = x - x_0
        y = y - y_0

        plt.quiver(x_0, y_0, x, y, angles="xy", scale_units="xy", scale=1, color=colr)
        x_vals.extend([int(x_0), int(x)])
        y_vals.extend([int(y_0), int(y)])

    plt.xlim(min(x_vals) - 1, max(x_vals) + 1)
    plt.ylim(min(y_vals) - 1, max(y_vals) + 1)

    plt.xticks(range(min(x_vals) - 1, max(x_vals) + 2))
    plt.yticks(range(min(y_vals) - 1, max(y_vals) + 2))

    plt.gca().set_aspect("equal")
    plt.grid()
    plt.show()


def find_linear_combination_coefficients(e1, e2, v):
    """
    Returns the coordinates of the representation of v in the basis {e_1, e_2}.
    That is, the unknown coefficients in the linear combination  v = lambda_1 * e_1 + lambda_2 * e_2:

    Research:
    x0 * e_1 + x1 * e_2 = v

    x0 * e_1[0] + x1 * e_2[0] = v[0]
    x0 * e_1[1] + x1 * e_2[1] = v[1]

    a = np.array([[e_1[0], e_2[0]], [e_1[1], e_2[1]])
    b = np.array([v[0], v[1]])
    x0, x1 = np.linalg.solve(a, b)


    Solution from research:
    https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html

    x0 + 2 * x1 = 1
    3 * x0 + 5 * x1 = 2
    a = np.array([[1, 2], [3, 5]])
    b = np.array([1, 2])
    x = np.linalg.solve(a, b)
    x
    """

    # Method 1:
    # e11 = e1[0]
    # e21 = e2[0]
    # e12 = e1[1]
    # e22 = e2[1]
    # a = np.array([[e11, e21], [e12, e22]])
    #
    # return np.linalg.solve(a, b)

    # Method 2:
    a = np.array([e1, e2])
    a.transpose()

    return np.linalg.solve(a, v)


# Plotting some vectors:
plot_vectors([[0, 0, 2, 3]], ["red"]) # One vector
plot_vectors([[0, 0, 1, 0], [0, 0, 0, 1]], ["red", "blue"]) # Two orthogonal vectors
plot_vectors([[1, 1, -2, 3], [2, 1, -2.5, 1.5], [-3.2, -1.5, 0, 4.3]], ["red", "blue", "orange"]) # Three arbitrary vectors

# Defining basis vectors:
e1, e2 = [[1, 0], [0, 1]]
v = [3.5, 8.6]

# Find the unknown coefficients. Extract the logic in a function.
# It should accept the two basis vectors and the one we need to represent
# and should return the two coefficients

coefficients = find_linear_combination_coefficients(e1, e2, v)
print("Coefficients: ", str(coefficients))
# Plot the three vectors
plot_vectors([[0, 0, i[0], i[1]] for i in [e1, e2, v]], ["red", "blue", "green"])

# Choosing different basis:
e1, e2 = [[2, 3], [-5, 1]]
coefficients = find_linear_combination_coefficients(e1, e2, v)
print("Coefficients: ", str(coefficients))
plot_vectors([[0, 0, i[0], i[1]] for i in [e1, e2, v]], ["red", "blue", "green"])

# Choosing orthogonal basis:
e1, e2 = [[3, 4], [-4, 3]]
coefficients = find_linear_combination_coefficients(e1, e2, v)
print("Coefficients: ", str(coefficients))
plot_vectors([[0, 0, i[0], i[1]] for i in [e1, e2, v]], ["red", "blue", "green"])

# Choosing collinear basis:
e1, e2 = [[0, 5], [4, 0]]
coefficients = find_linear_combination_coefficients(e1, e2, v)
print("Coefficients: ", str(coefficients))
plot_vectors([[0, 0, i[0], i[1]] for i in [e1, e2, v]], ["red", "blue", "green"])

