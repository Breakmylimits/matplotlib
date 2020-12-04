import matplotlib.pyplot as plt

def coffee():

    x = range(4)
    y = (20, 25, 40, 30)
    avg = sum(y)/4
    xtick = ("mocha","latte", "espresso", "tea")
    plt.bar(x,y, color="blue")
    plt.xticks(x ,xtick )
    plt.axhline(avg, color = "red", linestyle="--")
    plt.title("Order by menu \n Feb 2020", color="red", fontsize=18)
    plt.ylabel(" count order")
    plt.show()

if __name__ == "__main__":
    coffee()