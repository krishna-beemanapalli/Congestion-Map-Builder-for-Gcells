import numpy as np
import matplotlib.pyplot as plt
import math
import sys
# rng=np.random.RandomState(0)
# data=rng.randn(10,10)
np.set_printoptions(threshold=sys.maxsize)


pts = []
leftmost_x = float("inf")
leftmost_y = float("inf")
rightmost_x = float("-inf")
rightmost_y = float("-inf")

size = 50
data = np.zeros(shape=(size, size))
count = 0

if __name__ == "__main__":

	with open("routing3.guide", "r") as f:

		data1 = np.zeros(shape=(size, size))

		for line in f.readlines():
			vals = line.split(' ')

			if len(vals) == 1:
				data = data + data1
				count += 1
				data1 = np.zeros(shape=(size, size))

			if len(vals) == 5:
				x, y, a, b = float(vals[0]) / 10000, float(vals[1])/10000, float(vals[2]) / 10000, float(vals[3]) / 10000
				data1[int(x) : int(a + 1), int(y) : int(b + 1)] = 1

	print (data)

	plt.imshow(data, origin = 'lower')

	plt.show()
