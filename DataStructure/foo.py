from random import random

def foo(m, n, k):
	result = [[0] * n] * m
	boom = []
	while len(boom) < k:
		xaix = int(random() * n)
		yaix = int(random() * m)
		if [xaix, yaix] not in boom:
			result[xaix][yaix] = "B" 
			boom.append([xaix, yaix])


	for b_x, b_y in boom:
		if  b_x+1 < m:
			plus_one(result[b_x+1][b_y])
			if b_y+1 < n:
				plus_one(result[b_x+1][b_y+1])
			if b_y-1 >= 0:
				plus_one(result[b_x+1][b_y-1])
		if  b_x-1 >= 0:
			result[b_x-1][b_y] += 1
			if b_y+1 < n:
				plus_one(result[b_x-1][b_y+1])
			if b_y-1 >= 0:
				plus_one(result[b_x-1][b_y-1])

	if b_y+1 < n:
		plus_one(result[b_x][b_y+1])
	if b_y-1 >= 0:
		plus_one(result[b_x][b_y-1])
	return result

def plus_one(obj):
	if instance(obj, int):
		obj += 1


print(foo(10, 10, 9))