from sys import argv

script, first, second, third = argv

print "script name:", script
print "first variable:", first
print "second variable:", second
print "thirs variable:", third

name = first + ":"
age = second + ":"
sex = third + ":"
a1 = raw_input(name)
a2 = raw_input(age)
a3 = raw_input(sex)

print a1, a2, a3