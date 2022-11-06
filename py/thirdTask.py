import seaborn as sns
import matplotlib.pyplot as plt
import firstTask

#'age,sex,bmi,children,smoker,region,charges
inshuranceData = firstTask.getData()

#sns.histplot(data=inshuranceData['age'])
sns.histplot(data=inshuranceData['bmi'], kde=True)
#sns.histplot(data=inshuranceData['children'])
#sns.histplot(data=inshuranceData['charges'])

plt.show()