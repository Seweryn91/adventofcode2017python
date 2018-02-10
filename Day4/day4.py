#day4

def loader(file):
    '''loads words from inputfile'''

    with open(file) as rawfile:
        data = rawfile.read()
        return data

def day4_solve1(data):
	'''solves first puzzle'''
	data = [row.split() for row in data.splitlines()]
	count = 0
	for word in data:
		if len(word) == len(set(word)): #set = unordered collection with no duplicates
			count += 1

	print("Solution 1 is:",count)

day4_solve1(loader("day4.txt"))