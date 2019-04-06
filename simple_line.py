import datetime
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.size'] = 16

today = datetime.datetime.today().date()
num_days = 90
three_months = [today - datetime.timedelta(days=x) for x in range(num_days, 0, -1)]

y_data = sorted(list(np.random.rand(num_days)))
z_data = [2*x for x in np.random.rand(num_days)]

fig = plt.figure()
ax = fig.gca()
ax.bar(three_months, y_data, color='red', linestyle='solid', label='random sorted')
ax.plot(three_months, z_data, color='#0000FF', linestyle=':', label='2x random')
ax.legend(loc='upper left')
for tick in ax.get_xticklabels():
    tick.set_rotation('vertical')
ax.set_xlim(three_months[0], today)
ax.set_ylim(0, 2)
ax.set_title("Change over three months")
ax.set_ylabel("Some random value")
plt.show()

