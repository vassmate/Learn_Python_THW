# http://learnpythonthehardway.org/book/ex6.html


# It will put a decimal value in the string.
x = "There are %d types of people." % 10


# It will add a string as a value to the 'binary' variable.
binary = "binary"


# It will also add a string value to the variable.
do_not = "don't"


# This will put the two string variables into another string.
y = "Those who know %s and those who %s." % (binary, do_not)


# Printing the 'x' variable.
print x


# Printing the 'y' variable.
print y


# Printing the formatted 'x' variable.
# Also %r puts anything inside the string. The type of the variable does not matter.
print "I said: %r." % x


# Printing the formatted 'y' variable.
print "I also said '%s'." % y


# This gives the variable a 'bool' value.
hilarious = False


# This is just a string variable with a string formatting '%r' in it.
joke_evaluation = "Isn't that joke so funny?! %r"


# This prints out out the 'joke_evaluation' string variable and also places the bool variable in it.
# The formatting was already 'premade' in the 'joke_evaluation' variable,
# so we don't have to write everything down again.
print joke_evaluation % hilarious


# This makes a string variable.
w = "This is the left side of..."


# This is also makes a string variable.
e = "a string with a right side."


# This will print out the 'w' and 'e' variables result after adding them together.
print w + e