import numpy as np
import scipy.interpolate as si
from matplotlib import pyplot as plt

def bspline(cv,n,degree):
    """ bspline basis function
        c        = list of control points.
        n        = number of points on the curve.
        degree   = curve degree
    """
    # Create a range of u values
    c = cv.shape[0]
    kv = np.clip(np.arange(c+degree+1)-degree,0,c-degree)
    u  = np.linspace(0,c-degree,n)
   
    
    return np.array(si.splev(u, (kv,cv.T,degree))).T
# Control points
cv = np.array([[-1.,0.],
		[1.,4.],
		[3.,-2.],
		[4.,3.],
		[6.,1.]])
plt.plot(cv[:,0],cv[:,1], 'o-', label='Control Points')
colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')
n=100
degree = 3 # Curve degree
for d in range(1,4):
    p = bspline(cv,n,degree)
    x,y = p.T
    plt.plot(x,y,'k-',label='Degree %s'%d,color=colors[d%len(colors)])
plt.show()
