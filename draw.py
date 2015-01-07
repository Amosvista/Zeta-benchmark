import matplotlib.pyplot as plt


def draw(title, xlabel, xdata, ylabel, yedata, yzdata):
    plt.figure(figsize=(8, 4))
    plt.plot(xdata, yedata, label="Express", color="blue", linewidth=2, markersize=6)
    plt.plot(xdata, yzdata, color="green", label="Zeta", linewidth=2, markersize=6)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()
