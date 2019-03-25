import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.figure import Figure

"""
(1) Negative values only appear when the script traffic script is stopped
    then run again. The accumulated packets & bytes are reset and cause a 
    negative difference.
"""

style.use("ggplot")

fig = plt.figure("Network Traffic")
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    graph_data = open("flowDataset6.csv", "r")
    # skip first line
    next(graph_data)
    readData = graph_data.read()
    lines = readData.split("\n")
    xs = []  # Rx pkts
    ys = []  # Tx pkts
    ls = []  # Label
    # append the latest 100 data points
    for line in lines[-150:]:
        if len(line) > 1:
            x, y, a, b, l = line.split(",")
            # skip negative values (1)
            if int(x) < 0:
                pass
            else:
                xs.append(int(x))
                ys.append(int(y))
                ls.append(int(l))

    xAxis = list(range(0, len(xs)))
    ax1.clear()
    # set up title, axes, legend
    ax1.set_title("Network Traffic")
    ax1.set_xlabel("Data points")
    ax1.set_ylabel("Number of packets")
    ax1.plot(xAxis, xs, ".-", ys, ".-")
    # change the marker based on label
    for i in xAxis:
        # if "ddos" data point
        if ls[i] == 1:
            ax1.plot(xAxis[i], xs[i], "kx-", xAxis[i], ys[i], "kx-")

            # include another title stating 'currently being attacked' or something similar


ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show()
