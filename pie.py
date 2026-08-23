import matplotlib.pyplot as plt
names=["Product A","Product B","Product C","Product D"]
values=[31,20,34,15]
colors=["blue","lightpink","red","yellow"]
explode=[0.01,0.01,0.01,0.01]
plt.figure(figsize=(7,7))
plt.pie(values,labels=names,autopct="%1.1f%%",startangle=90,colors=colors,explode=explode,
        textprops={"fontweight": "bold","fontsize":12})
plt.title("MARKET SHARE BY PRODUCTS")
plt.axis("equal")
plt.tight_layout()
plt.show()

