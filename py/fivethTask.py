import firstTask
import matplotlib.pyplot as plt

#'age,sex,bmi,children,smoker,region,charges'
inshuranceData = firstTask.getData()

plt.figure(figsize=(5, 7))

#inshuranceData.boxplot()

#plt.boxplot(inshuranceData['age'], labels=['age'], vert=True)
#plt.boxplot(inshuranceData['bmi'], labels=['bmi'], vert=True)
#plt.boxplot(inshuranceData['children'], labels=['children'], vert=True)
plt.boxplot(inshuranceData['charges'], labels=['charges'], vert=True)

plt.grid()

plt.show()