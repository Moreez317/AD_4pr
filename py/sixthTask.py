import firstTask
import numpy as np
import matplotlib.pyplot as plt


inshuranceData = firstTask.getData()
bmiData = inshuranceData['bmi']

means32 = []
means128 = []
means512 = []

for i in range(300):
    sample = bmiData.sample(32)
    means32.append(sample.mean())

    sample = bmiData.sample(128)
    means128.append(sample.mean())

    sample = bmiData.sample(512)
    means512.append(sample.mean())

fig, ax = plt.subplots(1, 3)
ax[0].hist(means32, color='cyan', label='32', kde=True)
ax[0].set_title('32')
ax[1].hist(means128, color='magenta', label='128')
ax[1].set_title('128')
ax[2].hist(means512, color='yellow', label='512')
ax[2].set_title('512')

print(f"среднее bmi: {bmiData.mean()}")

print("выборка в 32 элементов:")
print(f"\tстандартное отклонение: {np.std(means32)}")
print(f"\tсреднее: {np.mean(means32)}")

print("выборка в 128 элементов:")
print(f"\tстандартное отклонение: {np.std(means128)}")
print(f"\tсреднее: {np.mean(means128)}")

print("выборка в 512 элементов:")
print(f"\tстандартное отклонение: {np.std(means512)}")
print(f"\tсреднее: {np.mean(means512)}")

plt.show()