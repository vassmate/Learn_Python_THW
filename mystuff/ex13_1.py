from sys import argv

script, number1 = argv

number2 = raw_input("Enter something: ")

number3 = "%s %s" % (number1, number2)

number4 = (int(number1) + int(number2))

print "This is the script: ", script
print "This is the argv: ", number1
print "This is the raw input: ", number2
print "This is the two string together: ", number3
print "This is the two string converted to integer and added together: ", number4