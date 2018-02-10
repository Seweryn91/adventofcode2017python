#day4

def loader(file = "day4.txt"):
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
	
	
def day4_solve2(data):
	'''solves second part checking each line (list).
	If line is valid it increments value of "count" variable'''
	data = [row.split() for row in data.splitlines()]
	count = 0
	for word in data:
		if is_line_valid(word):
			count += 1
	print("Number of valid non-anagram passphrases:", count)

def is_line_valid(word):
	'''checks line (list) for unique words apperance.
	example: for first line:
	0(index1) vxjtwn(word1) 1(index2) vjnxtw(word2)
	word1 and word2 are anagrams therefore are invalid = line returns False'''
	for index1, word1 in enumerate(word):
		for index2, word2 in enumerate(word):
			if index1 != index2 and are_words_anagrams(word1, word2):
				return False
	return True
	

def are_words_anagrams(word1, word2):
	'''checks if words are of the same lenght and contain the same letters'''
	return sorted(word1) == sorted(word2)

day4_solve1(loader())
day4_solve2(loader())
