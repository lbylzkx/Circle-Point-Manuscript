import matplotlib.pyplot as plt
import numpy as np


def arc(center, point1, point2, color='b'):
    # Calculate vectors from center to points
    vector1 = np.array(point1) - np.array(center)
    vector2 = np.array(point2) - np.array(center)

    # Calculate lengths of vectors
    r1 = np.linalg.norm(vector1)
    r2 = np.linalg.norm(vector2)

    # Calculate angles between vectors
    theta1 = np.arctan2(vector1[1], vector1[0])
    theta2 = np.arctan2(vector2[1], vector2[0])

    # Make sure theta2 > theta1
    if theta2 < theta1:
        theta2 += 2 * np.pi

    # Calculate points on arc
    t = np.linspace(theta1, theta2, 100)
    x = center[0] + r1 * np.cos(t)
    y = center[1] + r1 * np.sin(t)

    # Set X and Y axes equal length
    plt.axis('equal')
    # Plot arc
    plt.plot(x, y, color)


# Example usage
arc((0, 1), (2, 1), (1, 2), 'b')
arc((0, 1), (1, 2), (2, 1), 'b')
plt.show()
