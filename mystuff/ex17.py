# http://learnpythonthehardway.org/book/ex17.html

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

print "The input file %d bytes long." % len(indata)

print "Doeas the output file exist? %r" % exists(to_file)
print "Ready, hit REATURN to continue, CTRL_C TO abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()