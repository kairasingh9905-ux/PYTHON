import matplotlib.pyplot as plt
days=[1,2,3,4,5]
stock=[150.4,143.8,177.0,129.7,135.9]
plt.plot(days,stock,marker="o",color="red",linestyle="--",linewidth=4)
plt.xlabel("DAYS")
plt.ylabel("STOCK VALUES")
plt.title("STOCK VALUES OVER 5 DAYS")
plt.grid(True ,alpha=0.3)
plt.tight_layout()
plt.show()