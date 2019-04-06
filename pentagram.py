from matplotlib import patches
from math import pi, sqrt
from matplotlib.path import Path
import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))

def pentagon(radius, orientation):
    return patches.RegularPolygon((0,0), numVertices=5, radius=radius, orientation=orientation, linestyle='-', fill=None)

def get_pentagon_vertices(pentagon):
    return [(x[0], x[1]) for x in pentagon.get_verts()]

_, ax = plt.subplots()
outer_radius = 10.0
inner_radius = 2.0/(3.0+sqrt(5.0))*outer_radius + 2
ax.set_aspect(1)
ax.set_xlim(-outer_radius, outer_radius)
ax.set_ylim(-outer_radius, outer_radius)
outer_pentagon = pentagon(outer_radius, 0)
outer_points = get_pentagon_vertices(outer_pentagon)
#ax.add_artist(outer_pentagon)
inner_pentagon = pentagon(inner_radius, pi/5.0)
inner_points = get_pentagon_vertices(inner_pentagon)
#ax.add_artist(inner_pentagon)
ax.set_axis_off()

star_points = []
for idx in range(len(outer_points)):
    star_points.append(outer_points[idx])
    star_points.append(inner_points[idx])

codes = [Path.MOVETO] + [Path.LINETO]*(len(star_points)-2) + [Path.CLOSEPOLY]
star = Path(star_points, codes)
patch = patches.PathPatch(star, facecolor='orange', lw=2)
ax.add_patch(patch)
plt.show()

