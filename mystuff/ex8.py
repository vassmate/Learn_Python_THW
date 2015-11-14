formatter = "%r %r %r %r"


print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.", 
	"That you could type up right.", 
	"But it didn't sing.",
	"So I said goodnight."
)

# The '%r' is for debugging,
# so it doesn't always prints out the string exactly as you defined it (aka with double-quotes).
# That's why we get back sometimes single-quotes insted of double-quotes on the interpreter.