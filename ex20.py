from sys import argv

#script, filename = argv
filename = "ex15_sample.txt"

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)
	
def print_line(line_num, f):
	print line_num, " ", f.readline(),
	
input_file = open(filename)

print_all(input_file)

rewind(input_file)

line_num = 0
print_line(line_num, input_file)

line_num += 1
print_line(line_num, input_file)

line_num += 1
print_line(line_num, input_file)

input_file.close()