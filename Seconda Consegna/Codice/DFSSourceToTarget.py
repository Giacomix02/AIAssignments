
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
from graphPlot import Graph
import dfs

fig = plt.figure("DFS")
ax = fig.add_subplot(111)
plt.title("DFS")
plt.xlim([0, 9])
plt.ylim([0, 9])
plt.xlabel("x - axis")
plt.ylabel("y - axis")



# def scrivi(x,y,n):
#     rectGoal = rettangoli[x][y]
#     xy = rectGoal.get_xy()
#     cx = xy[0] + rectGoal.get_width() / 2
#     cy = xy[1] + rectGoal.get_height() / 2
#     ax.annotate(n, (cx, cy), color='black', weight='bold', fontsize=16, ha='center', va='center')

class Square(Rectangle):
    _numero: int
    _visitato: bool
    _ostacolo: bool
    _tipo: int          # 1 = inizio, 2 = fine, 0 = qualsiasi nodo
    _x: int
    _y: int

    def __init__(self, ostacolo, x, y, tipo:int):
        self._visitato = False
        self._ostacolo = ostacolo
        self._x = x
        self._y = y
        self._tipo = tipo

        if ostacolo:
            super().__init__((x, y), 1, 1, color='black', fc='black', lw=2)
        else:
            if(self._tipo==1):
                super().__init__((x, y), 1, 1, color='black', fc='red', lw=2)
            if(self._tipo==2):
                super().__init__((x, y), 1, 1, color='black', fc='green', lw=2)
            else:
                super().__init__((x, y), 1, 1, color='black', fc='none', lw=2)


    def get_visitato(self):
        return self._visitato
    def set_visitato(self, visitato):
        self._visitato = visitato
    def get_ostacolo(self):
        return self._ostacolo
    def coordinate(self):
        return (self._x, self._y)

    def set_numero(self, numero):
        self._numero = numero

    def get_numero(self):
        return self._numero


def ostacolo(i,j):
    if(j==5 and (3<=i<=7)):
        return True
    if(j==4 and i==2):
        return True
    if(j==3 and (i==3 or i==7)):
        return True
    return False

def tipo( i, j):
    if(j==6 and i==3):
        return 2
    if(j==3 and i==4):
        return 1
    else:
        return 0


rettangoli = []

for i in range(0, 8):
    row = []
    for j in range(0, 8):
        row.append(Square(ostacolo(i + 1, j + 1), i + 1, j + 1, tipo(i + 1, j + 1)))
    rettangoli.append(row)

for i in range(len(rettangoli)):
    for j in range(len(rettangoli[i])):
        ax.add_patch(rettangoli[i][j])

def animate(p):
    global rettangoli
    for k in range(rettangoli.__len__()):
        for j in range(rettangoli[k].__len__()):
            if rettangoli[k][j]._visitato or rettangoli[k][j]._tipo==1:
                rettangoli[k][j].set_color('red')
            elif rettangoli[k][j]._ostacolo:
                rettangoli[k][j].set_color('black')
            else:
                rettangoli[k][j].set_edgecolor("black")


ani = animation.FuncAnimation(
    fig, animate,
    frames=1,
    # blit=True, save_count=50,
    interval=100
)

rect = rettangoli[3][2]
xy = rect.get_xy()
cx = xy[0] + rect.get_width() / 2
cy = xy[1] + rect.get_height() / 2
ax.annotate("s", (cx, cy), color='black', weight='bold', fontsize=16, ha='center', va='center')

rect = rettangoli[2][5]
xy = rect.get_xy()
cx = xy[0] + rect.get_width() / 2
cy = xy[1] + rect.get_height() / 2
ax.annotate("g", (cx, cy), color='black', weight='bold', fontsize=16, ha='center', va='center')


Graph()

dfs.dfs(rettangoli, rectStart, rectGoal)  # esegue la dfs sulla griglia

plt.show()
