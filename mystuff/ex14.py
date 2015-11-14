# http://learnpythonthehardway.org/book/ex14.html

from sys import argv

script, user_name, age = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What kind of pet do you have?"
pet = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
You are %r years old and have a %r as a pet.
Also you have a %r computer. Nice.
""" % (likes, lives, age, pet, computer)