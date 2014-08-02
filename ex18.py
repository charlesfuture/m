def print_two(*arg):
	arg1, arg2 = arg
	print "arg1:%r, arg2:%r" % (arg1, arg2)

def print_2_again(arg1, arg2):
	print "arg1:%r, arg2:%r" % (arg1, arg2)
	
def print_one(arg):
	print "arg: %r" % arg
	
def print_none():
	print "I got noting"
	
print_two("aq", "ws")
print_2_again("de", "fr")
print_one(123)
print_none()