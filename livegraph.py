import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.figure import Figure

style.use("ggplot")

fig = plt.figure("Network Traffic")
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    graph_data = open("tester.csv", "r").read()
    lines = graph_data.split("\n")
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y, a, b = line.split(",")
            xs.append(int(x))
            ys.append(int(y))

    xAxis = list(range(0, len(xs)))
    ax1.clear()
    # set up title, axes, legend
    ax1.set_xticks(xAxis)
    ax1.set_title("Network Traffic")
    ax1.set_xlabel("Data points")
    ax1.set_ylabel("Number of packets")
    ax1.plot(xAxis, xs, "-v", ys, "-v")
    # change the marker based on label
    for i in xAxis:
        if xs[i] > 200:
            ax1.plot(xAxis[i], xs[i], "bo-", xAxis[i], ys[i], "ro-")


ani = animation.FuncAnimation(fig, animate, interval=2000)
plt.show()
