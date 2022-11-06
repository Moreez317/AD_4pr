import firstTask
import statsmodels.api as sm
import matplotlib.pyplot as plt
import scipy.stats as stats

inshuranceData = firstTask.getData()
bmi = inshuranceData['bmi']
charges = inshuranceData['charges']

sm.qqplot(bmi)
sm.qqplot(charges)

plt.show()

stdBmiData = (bmi - bmi.mean())/bmi.std()
stdChargesData = (charges - charges.mean())/charges.std()

print('BMI: ', stats.kstest(stdBmiData, 'norm'))
print('Charges: ', stats.kstest(stdChargesData, 'norm'))
