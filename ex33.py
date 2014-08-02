#i = 0
numbers = []

#while i < 6:
#	print 'The current i is: %d' % i
#	numbers.append(i)
#	print 'The current Numbers is:', numbers
	
#	i = i + 1

def loop(a, b):
	i = 0
	while i < a:
		print i
		numbers.append(i)
		print numbers
		
		i = i+b

loop(10, 2)

for a in range(0,6):
	numbers.append(a)

for num in numbers:
	print num


