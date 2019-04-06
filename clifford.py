import pandas as pd
import datashader as ds
from datashader import transfer_functions as tf
from datashader.colors import inferno, viridis
from numba import jit
from math import sin, cos, sqrt, fabs

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

@jit
def Clifford(x, y, a, b, c, d, *o):
    return sin(a * y) + c * cos(a * x), \
           sin(b * x) + d * cos(b * y)

N=10000000

@jit
def trajectory(fn, x0, y0, a, b=0, c=0, d=0, e=0, f=0, n=N):
    x, y = np.zeros(n), np.zeros(n)
    x[0], y[0] = x0, y0
    for i in np.arange(n-1):
        x[i+1], y[i+1] = fn(x[i], y[i], a, b, c, d, e, f)
    return pd.DataFrame(dict(x=x,y=y))

df = trajectory(Clifford, 0, 0, -1.3, -1.3, -1.8, -1.9)
cvs = ds.Canvas(plot_width = 700, plot_height = 700)
agg = cvs.points(df, 'x', 'y')
ds.transfer_functions.Image.border=0

tf.shade(agg, cmap=['white', 'navy'])

