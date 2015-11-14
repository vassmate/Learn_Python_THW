def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def do_the_math(num1, num2):
	print "Number one: %d" % num1
	print "Number two: %d" % num2
	print "The result when you add them together: %d" % (num1 + num2)
	print "The result when you divide them: %d" % (num1 / num2)
	print "And that's it!\n"


print "Simple call:"
do_the_math(15, 20)


print "Calling with variables:"
n1 = 12
n2 = 24

do_the_math(n1, n2)


print "Operations in the arguments:"
do_the_math(15 + 12, 24 - 20)

print "Operations in the arguments with variables:"
do_the_math(n1 + n2, n2 - 4)
