import numpy as np
import matplotlib.pyplot as plt


"""For bifurcation diagrams"""

def generate_x(r, x0 = .5, M =10000):  
    x = [x0]
  
    for i in range(1, M):
        x.append(r * x[i-1] * (1 - x[i-1]))
        
    return x 

#find attractors for a single r value
def find_attractors(r, x0 = .5, M = 10000, cutoff = 8000, dec = 4):
	x = generate_x(r, x0, M)
	attractors = np.unique(np.round(x[cutoff:], dec))
	corr_r = [r for val in range(len(attractors))]

	return corr_r, attractors

	
#make arrays to plot
def make_arrays(r_i = 2.8, r_f = 4., h = .01, dec = 4):
	attractors = []
	corr_r = []

	r = np.arange(r_i, r_f + h, h)

	for i in range(len(r)):
		temp_r, temp_att = find_attractors(r[i], dec = dec)
		attractors.extend(temp_att)
		corr_r.extend(temp_r)

	return corr_r, attractors


"""For finding attractors"""

fx = lambda r, x = np.linspace(0.,1., 10000) : r * x * (1 - x)

ffx = lambda r : fx(r, fx(r))

def find_intersections(f, g):
	intersections = []
	diffs = f-g

	for i in range(len(f) - 1):
		if diffs[i] == 0 or diffs[i]*diffs[i+1] < 0:
			intersections.append(i)

	return intersections


def prep_arrays_40(f, h = .001):
	r = np.arange(0, 4.1, h)
	x_t = np.linspace(0., 1., 10000) #45 degree line
	corr_r = [] # for the r-values corresponding to each fixed point
	ints = []

	for i in range(len(r)):
		temp_ints = find_intersections(f(r[i]), x_t)
		ints.extend(x_t[temp_ints])

		for j in range(len(temp_ints)):
			corr_r.append(r[i])

	return corr_r, ints