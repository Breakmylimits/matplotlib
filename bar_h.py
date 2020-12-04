import matplotlib.pyplot as plt

def bar_h():
    x = range(4)
    y = (20, 25, 40, 30)
    xticks = ("mocha", "latte", "espresso", "tea")
    plt.yticks(x , xticks)
    plt.barh(x, y)
    plt.show()

def bar_subplot():
    x = range(4)
    y = (20, 25, 40, 30)
    ysum = sum(y)/4
    xticks = ("mocha", "latte", "espresso", "tea")
    fig, ax = plt.subplots(1,2)
    ax[0].bar(x, y, color="green")
    ax[1].barh(x, y, color="purple")
    plt.sca(ax[0])
    plt.xticks(x ,xticks)
    plt.sca(ax[0])
    plt.axhline(ysum, color="red",  linestyle="--")
    plt.sca(ax[1])
    plt.yticks(x ,xticks)
    plt.sca(ax[1])
    plt.axvline(ysum, color="red",  linestyle="--")
    fig.tight_layout()
    
    plt.show()


if __name__ == "__main__":
    bar_subplot()

