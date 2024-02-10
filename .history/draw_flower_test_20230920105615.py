import matplotlib.pyplot as plt
from draw_arc import arc
from draw_circle_by_point import *

# arc((0, 1), (2, 1), (1, 2))
# arc((0, 0), (-1, -1), (1, 1))

arc((-0.5, -0.5), (0, 1), (-1, 1), 'r')
arc((-0.5, 0), (0.5, 0.5), (0, 1), 'b')
plt.show()
