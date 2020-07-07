import numpy as np
from scipy.special import comb
from matplotlib import pyplot as plt

def bernstein_poly(i, n, t):

	return comb(n, i) * ( t**(n-i) ) * (1 - t)**i

def bezier_curve(points, nTimes=1000):
	nPoints = len(xpoints)
	xPoints = np.array([p[0] for p in points])
	yPoints = np.array([p[1] for p in points])
	
	t = np.linspace(0.0, 1.0, nTimes)
	
	polynomial_array = np.array([ bernstein_poly(i, nPoints-1, t) for i in range(0, nPoints) ])
	
	xvals = np.dot(xPoints, polynomial_array)
	yvals = np.dot(yPoints, polynomial_array)
	
	return xvals, yvals

if __name__ == "__main__":
	nPoints = 4
	points = np.array([[-3,0],
				[-1,4],
				[2,3],
				[4,1]])
	xpoints = [p[0] for p in points]
	ypoints = [p[1] for p in points]
	xvals, yvals = bezier_curve(points, nTimes=1000)
	plt.plot(xvals, yvals)
	plt.plot(xpoints, ypoints, "ro")
	for nr in range(len(xpoints)):
		plt.text(points[nr][0], points[nr][1], nr)
	plt.show()
