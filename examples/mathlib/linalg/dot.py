from ..ndarray import sum1d

def dot1d(array_a, array_b):
	return sum1d([array_a[i] * array_b[i] for i in xrange(len(array_a))])