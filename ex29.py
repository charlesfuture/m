a = 30
b = 20
c = 50

if c == a + b:
	print "c == a + b"
elif c != a + b:
	print "c != a + b"
else:
	print 0

if a < b:
	print "a < b"
elif a > b:
	print "a > b"
else:
	print "a = b"

if a > b:
	print "a > b"
elif a < b:
	print "a < b"
else:
	print "a = b"

a = int(raw_input('> '))
if a == 1 or a == 2:
	print a
elif a == 3:
	print "a = 3"
else:
	if a > 10:
		print "hahaha"
	else:
		print "huhuhu"