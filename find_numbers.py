import itertools


'''
numbers to fill in: 1,3,5,7

Place the missing numbers
	 2??8
	+?456
	 ?174
'''


def solve():
	
	possible_numbers = [1,3,6,7]
	
	string = '2??8+?456==?174'
	
	possibilities = itertools.permutations(possible_numbers)
	for each_possibility in possibilities:
		new_string = string
		for each_number in each_possibility:
			new_string = new_string.replace('?', str(each_number), 1)
		if eval(new_string):
			print(new_string)

solve()
