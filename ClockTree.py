import math

Graph = {}

def mmm(pts, cut_direction):

	if len(pts) == 1:
		Graph[tuple(pts[0])] = []
		return pts[0]

	pts = pts[:] # clone the points

	pts.sort(key = lambda x : x[cut_direction])
	
	mid = int(len(pts) / 2)
	left_pts = pts[:mid]
	right_pts = pts[mid: ] 

	left_median = mmm(left_pts, 1 - cut_direction)
	right_median = mmm(right_pts, 1 - cut_direction)

	new_median = [(left_median[0] + right_median[0]) / 2.0,
				  (left_median[1] + right_median[1]) / 2.0]

	print ("points: ", end="")
	for pt in pts:
		print (str(pt), end=""),

	print (" median: ", end="")
	print (new_median)

	Graph[tuple(new_median)] = [tuple(left_median), tuple(right_median)]

	return new_median

def find_shortest_distance(pt):
	
	pt = tuple(pt)
	if len(Graph[pt]) == 0:
		return 0

	left_pt = Graph[pt][0]
	right_pt = Graph[pt][1]

	return min(dist(left_pt, pt) + find_longest_distance(left_pt),
			   dist(right_pt, pt) + find_longest_distance(right_pt))

def dist(pt1, pt2):

	x1 = pt1[0]
	x2 = pt2[0]

	y1 = pt1[1]
	y2 = pt2[1]

	return abs(math.sqrt((x1 - x2) * (x1 - x2) + (y2 - y1) * (y2 - y1)))



def find_longest_distance(pt):

	pt = tuple(pt)
	if len(Graph[pt]) == 0:
		return 0

	left_pt = Graph[pt][0]
	right_pt = Graph[pt][1]

	return max(dist(left_pt, pt) + find_longest_distance(left_pt),
			   dist(right_pt, pt) + find_longest_distance(right_pt))


if __name__ == "__main__":
	pts = []
	with open("net4", "r") as f:
		for line in f.readlines():
			line = line.strip()
			line = line.split(' ')
			pts.append([float(line[0]), float(line[1])])

	central_median = mmm(pts, 1)

	print(find_shortest_distance(central_median))
	print(find_longest_distance(central_median))
	print(find_longest_distance(central_median)-find_shortest_distance(central_median))






