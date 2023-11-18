# import networkx as nx
# import matplotlib.pyplot as plt


# g = nx.Graph()
# g.add_edge(1, 2)
# g.add_node(3)
# nx.draw_planar(g, with_labels = True)

# plt.title("test")

# plt.show()

# g.add_node(6)

# nx.draw_planar(g, with_labels = True)

# plt.figure().add_subplot(111)
from contextlib import _RedirectStream
import time
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# X = np.arange(16).reshape(4, 4)


fig = plt.figure()
ax = fig.add_subplot(111)
plt.title("DFS")
plt.xlim([0, 9])
plt.ylim([0, 9])
plt.xlabel("x - axis")
plt.ylabel("y - axis")


# rect1 = patches.Rectangle((1,1), 1, 1, color='black', fc = 'none',lw = 2)


# ax.add_patch(rect1)


class Square():
    _visitato: bool
    _ostacolo: bool
    _x: int
    _y: int
    _rettangolo: Rectangle

    def __init__(self, ostacolo, x, y):
        self._visitato = False
        self._ostacolo = ostacolo
        self._x = x
        self._y = y

        if (ostacolo):
            self._rettangolo = Rectangle((x, y), 1, 1, color='black', fc='black', lw=2)
        else:
            self._rettangolo = Rectangle((x, y), 1, 1, color='black', fc='none', lw=2)

    def get_visitato(self):
        return self._visitato

    def set_visitato(self, visitato):
        self._visitato = visitato

    def get_ostacolo(self):
        return self._ostacolo

    def coordinate(self):
        return (self._x, self._y)

    def disegna(self):
        return self._rettangolo


rettangoli = [[Square(False, i, j) for i in range(9)] for j in range(9)]

for i in range(len(rettangoli)):
    for j in range(len(rettangoli[i])):
        ax.add_patch(rettangoli[i][j].disegna())


def animate(k):
    global rettangoli
    for i in range(rettangoli.__len__()):
        for j in range(rettangoli[i].__len__()):
            if rettangoli[i][j]._visitato:
                rettangoli[i][j].disegna().set_color('red')
            elif rettangoli[i][j]._ostacolo:
                rettangoli[i][j].disegna().set_color('black')
            else:
                rettangoli[i][j].disegna().set_color('none')
    # rect1.set_color('red')
    return


ani = animation.FuncAnimation(
    fig, animate, frames=20, blit=True, save_count=50)

ani

plt.show()

