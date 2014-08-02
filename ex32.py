the_count = [1, 2, 3, 4, 5]
fruits = ["oranges", "apples", "bananas", "pears"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

for number in the_count:
	print "This is count %d" % number

for fruit in fruits:
	print "A fruit type is %r" % fruit

for i in change:
	print "I got %r" % i

a = range(0, 6)
elements = []

for i in a:
	print i
	elements.append(i+1)

for i in elements:
	print i

print len(elements)
