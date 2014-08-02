def secret(start_point):
	a = start_point * 500
	b = a / 1000
	c = b / 100
	return a, b, c

start_point = 10000;
a, b, c = secret(start_point)
print "%d, %d, %d" % (a, b, c)

print "%d, %d, %d" % secret(1000)