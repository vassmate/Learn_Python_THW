# http://learnpythonthehardway.org/book/ex15.html

print "Please enter the file name here: "
filename = raw_input("> ")

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

txt.close()