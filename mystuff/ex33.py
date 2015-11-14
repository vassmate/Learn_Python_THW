numbers = []

def list_maker(nums):
	ends_before = 10
	stepping = 1
	
	for i in range(0, ends_before, stepping):
		print "At the top i is %d" % i
		nums.append(i)
		
		print "Numbers now: ", nums
		print "At the bottom i is %d" % i


def print_list(nums):
	print "The numbers: "

	for num in nums:
		print num


list_maker(numbers)

print_list(numbers)