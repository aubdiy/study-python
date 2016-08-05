# this one is like your scripts with argv
def print_two(*args):
	arg0=args[0]
	# arg1=args[1]
	# arg2=args[1]
	arg1, arg2 =args
	print "arg0: %r, arg1: %r, arg2: %r" % (arg0, arg1, arg2)
# ok, that *args is actually pointless, we can just do this
def print_two_agian(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
	print "I got nothing."

print_two("Zed", "Shaw")
print_two_agian("Zed", "Shaw")
print_one("First!")
print_none()