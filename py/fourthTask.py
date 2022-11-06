import matplotlib.pyplot as plt
import firstTask

#'age,sex,bmi,children,smoker,region,charges'
inshuranceData = firstTask.getData()
bmi = inshuranceData['bmi']
charges = inshuranceData['charges']

def bmiInfo(inshuranceData):
    print("mean, median, mode: ", inshuranceData['bmi'].mean(), inshuranceData['bmi'].median(), inshuranceData['bmi'].mode())

    ax = bmi.hist(color="grey", edgecolor="black", linewidth=1.5)

    ax.axvline(bmi.mean(), color="red", label="mean")
    ax.axvline(bmi.mode()[0], color="green", label="mode")
    ax.axvline(bmi.median(), color="blue", label="median")
    ax.legend()


def chargesInfo(inshuranceData):
    print("mean, median, mode: ", inshuranceData['charges'].mean(), inshuranceData['charges'].median(), inshuranceData['charges'].mode())

    ax = charges.hist(color="grey", edgecolor="black", linewidth=1.5)

    ax.axvline(charges.mean(), color="red", label="mean")
    ax.axvline(charges.mode()[0], color="green", label="mode")
    ax.axvline(charges.median(), color="blue", label="median")
    ax.legend()


#bmiInfo(inshuranceData)
chargesInfo(inshuranceData)

plt.grid()
plt.show()