from sys import argv

script, filename = argv

print "If you don't want to erase the file, type ctrl-c"
print "If you want to do this, press ENTER"

raw_input("?")

file = open(filename, 'r+')
#file.truncate()

print "Now the file %r has been erased" % filename

print "Let's write something new to it!"

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

#file.write(line1)
#file.write('\n')
#file.write(line2)
#file.write('\n')
#file.write(line3)
#file.write('\n')

lines = (line1 + "%s" + line2 + "%s" + line3 + "%s") %("\n","\n","\n")
#file.write(lines)
print "OK, finished! We close it"

#file.close()

#file = open(filename, 'r')
print "Now the content of the file is:"
print file.read()

file.close()