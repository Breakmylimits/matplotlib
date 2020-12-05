import matplotlib.pyplot as plt
import numpy as np

def pie():
    label = ("china", "russia", "japan", "korea")
    val = (1.8, 1, .8, .5)
    plt.pie(val, labels=label, startangle=45, autopct= "%1.2f%%", explode=(0,0,0.1,0))
    plt.axis("equal")
    plt.show()

def pie2():
    label = np.array(["china", "russia", "japan", "korea"])
    val = (1.8, 1, .8, .5)
    explode = np.zeros(label.size)
    explode[2]=.1
    explode[np.where(label=="korea")]=.1
    colors = ["red","green", "pink", "orange" ]
    plt.pie(val, labels=label, startangle=45, autopct= "%1.2f%%", explode=explode, colors=colors)
    
    plt.axis("equal")
    plt.show()



if __name__ == "__main__":
    
    pie2()