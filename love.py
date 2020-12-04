import matplotlib.pyplot as plt

def love():
    a = int(input('Cinema :'))
    b = int(input('sea :'))
    c = int(input('temple :'))
    d = int(input('Amusement park :'))
    e = int(input('The park :'))
    y=[a,b,c,d,e]
    x=['Cinema', 'sea', 'temple', 'Amusement park', 'The park']
    plt.plot(x,y, color="red", linestyle="--", marker="o")
    plt.title("Place to be with your lover on Valentine's Day")
    plt.ylabel("people")
    plt.xlabel("place")
    plt.show()

if __name__ == "__main__":
    love()
