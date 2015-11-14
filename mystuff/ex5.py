# http://learnpythonthehardway.org/book/ex5.html


name = 'Zed A. Shaw'
age = 35
height = 74.0 #inches
weight = 180.0 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


height_in_centimeters = height * 2.54
weight_in_kilograms = weight / 2.2046


print "Let's talk about %s." % name
print "He's %d inches tall.(That's exactly %r in centimeters.)" % (height, height_in_centimeters)
print "He's %d pounds heavy (That's exactly %r in kilograms.)." % (weight, weight_in_kilograms)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth


print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + weight + height)