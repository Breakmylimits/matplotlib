import matplotlib.pyplot as plt
import numpy as np

def Combochart():
    labels=np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jan"])
    x = np.arange(labels.size)
    y1 = np.random.normal(80, 10, x.size)
    y2 = np.random.normal(95, 12, x.size)
    plt.bar(x, y1, color="deepskyblue", alpha=.3, label="we") #ค่าอัลฟาคือการทำทรานเพเร้นสีกราฟแท่ง
    plt.plot(x, y2, color="orange", label="industry" , marker="o")
    plt.xticks(x, labels)
    plt.legend()
    plt.title("Sales (Jan-Jun 2020)")
    plt.ylabel("sales (1000)")
    plt.show()
    

if __name__ == "__main__":
    Combochart()