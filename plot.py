import matplotlib.pyplot as plt
import parseData as d


def plot(title, ylabel, Url, KeyFeature):
    black = [0, 0, 0]

    def draw(title, xlabel, xdata, ylabel, yedata, yzdata):
        plt.figure(figsize=(8, 4))
        plt.plot(xdata, yedata, label="Express", color="blue", linewidth=2,
                 markersize=7, marker='o', mfc=black)
        plt.plot(xdata, yzdata, color="green", label="Zeta", linewidth=2,
                 markersize=7, marker='o', mfc=black)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.legend(loc=4)
        plt.show()
    data = d.bmData()
    draw(title, 'Concurrency (Number of Users in the same time)',
         data.concurrency, ylabel,
         d.get('express', Url, KeyFeature),
         d.get('zeta', Url, KeyFeature))
