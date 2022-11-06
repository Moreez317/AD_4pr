import firstTask
import scipy.stats as st
import numpy as np

#https://www.codecamp.ru/blog/plot-confidence-interval-python/

inshuranceData = firstTask.getData()
bmi = inshuranceData['bmi']
charges = inshuranceData['charges']

bmi_ci_95 = st.norm.interval(0.95, loc=np.mean(bmi), scale = st.sem(bmi))
charges_ci_95 = st.norm.interval(0.95, loc=np.mean(charges), scale = st.sem(charges))

bmi_ci_99 = st.norm.interval(0.99, loc=np.mean(bmi), scale = st.sem(bmi))
charges_ci_99 = st.norm.interval(0.99, loc=np.mean(charges), scale = st.sem(charges))

print('bmi ci 95%, 99%:', np.round(bmi_ci_95, 5), np.round(bmi_ci_99, 5))
print('charges ci 95%, 99%: ', np.round(charges_ci_95, 5), np.round(charges_ci_99, 5))

