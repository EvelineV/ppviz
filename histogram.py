import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sps

plt.rcParams['font.size'] = 16
counts = {}
dists = {}

x_axis = np.linspace(0, 10, 500)

for idx, (loc, scale) in enumerate([(4, 1.5), (7, 0.5)]):
    counts['source_{idx}'.format(idx=idx)] = sps.norm.rvs(loc=loc, scale=scale, size=1000)
    dists['source_{}'.format(idx)] = sps.norm.pdf(x_axis, loc=loc, scale=scale)


plt.figure(figsize=(8,6))
for k, v in counts.items():
    plt.hist(v, bins=50, range=(0, 10), histtype='step', density=1, label='sample {}'.format(k), linewidth=2)
    plt.plot(x_axis, dists[k], label='pdf {}'.format(k))
plt.xlim(0, 10)
plt.legend(loc='upper left')
plt.xlabel('Variable [unit]')
plt.ylabel('Relative frequency')
plt.grid(True)
plt.show()

