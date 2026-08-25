import numpy as np
import matplotlib.pyplot as plt
students=np.array(["Krish","Shreya","Astha","Avni","Vicky"])
subjects=np.array(["maths","physics","chemistry","english","cs"])
marks=np.array([[98,95,86,87,84],
               [87,67,87,94,86],
               [85,74,55,78,76],
               [87,56,66,85,78],
               [67,74,84,78,86]])
average_s=marks.mean(axis=0)
average_m=marks.mean(axis=1)
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.bar(students,average_m,color="blue")
plt.title("Students vs subject avg marks")
plt.ylabel("average marks")
plt.subplot(1,2,2)
plt.bar(subjects,average_s,color="red")
plt.title("Average marks per subject")
plt.ylabel("average marks")
plt.tight_layout()
plt.show()











