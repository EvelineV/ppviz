import matplotlib.pyplot as plt
from matplotlib.patches import Wedge

fig, ax = plt.subplots()
ax.set_aspect(1) # make the figure square

angle1 = 90
angle2 = angle1 + 180
center = (0, 0)
radius = 1
yin_color='white'
yang_color='black'

left_half_circle = Wedge(center, radius, angle1, angle2, color=yin_color)
right_half_circle = Wedge(center, radius, angle2, angle1, color=yang_color)
ax.add_artist(left_half_circle)
ax.add_artist(right_half_circle)

upper_big_circle = plt.Circle((0, 0.5), 0.5, color=yin_color)
ax.add_artist(upper_big_circle)
lower_big_circle = plt.Circle((0, -0.5), 0.5, color=yang_color)
ax.add_artist(lower_big_circle)

upper_small_circle = plt.Circle((0, 0.5), 0.1, color=yang_color)
ax.add_artist(upper_small_circle)
lower_small_circle = plt.Circle((0, -0.5), 0.1, color=yin_color)
ax.add_artist(lower_small_circle)

ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_axis_off()

border_circle = plt.Circle(center, radius+0.07, color=yang_color, fill=False, linewidth=5)
ax.add_artist(border_circle)

fig.tight_layout()
fig.savefig('yinyang.png', dpi=600, format='png', bbox_inches='tight')
