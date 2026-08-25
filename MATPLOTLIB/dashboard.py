import numpy as np
import matplotlib.pyplot as plt
name=np.array(["kabir","krish","avni","garima","kush"])
subject=np.array(["maths","physics","chemistry"])
marks=np.array([[78,67,56],
                [76,45,55],
                [87,86,56],
                [67,78,45],
                [66,76,87]])
average_student=marks.mean(axis=1)
average_subject=marks.mean(axis=0)
plt.figure(figsize=(15,9))
#for bar chart 1
plt.subplot(2,3,1)
plt.bar(name,average_student,color="skyblue")
plt.title("average marks per student")
plt.xlabel("names")
plt.ylabel("average marks")
#bar chart 2
plt.subplot(2,3,2)
plt.bar(subject,average_subject,color="lightgreen")
plt.title("average marks per subject")
plt.xlabel("subjects")
plt.ylabel("average marks")
#for pie chart
plt.subplot(2,3,3)
plt.pie(average_subject,labels=subject,autopct="%1.1f%%",
        colors=["red","blue","yellow"])
plt.title("average marks per subjects")
#line chart
plt.subplot(2,3,4)
for i,student_name in enumerate(name):
    plt.plot(subject,marks[i],marker="o",label=student_name)
plt.title("marks trend per student")
plt.xlabel("name")
plt.ylabel("marks")
plt.legend(fontsize=8)
#for scatter plot
plt.subplot(2,3,5)
plt.scatter(marks[:,0],marks[:,1],color="purple",s=80)
for i, student_name in enumerate (name):
    plt.annotate(student_name,(marks[i,0],marks[i,1]),textcoords="offset points",
    xytext=(5,5),fontsize=8 )
plt.title("maths vs physics marks")
plt.xlabel("maths marks")
plt.ylabel("physics marks")
#for histogram
plt.subplot(2,3,6)
plt.hist(marks.flatten(),bins=6,color="orange",edgecolor="black")
plt.title("distribution of all marks")
plt.xlabel("marks")
plt.ylabel("frequency")
#layout
plt.tight_layout()
plt.savefig("dashboard.png",dpi=150)
plt.show()




