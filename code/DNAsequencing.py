import collections
import time
import functools

class memoized(object):

	def __init__(self, func):
		self.func = func
		self.cache = {}
	def __call__(self, *args):
		if not isinstance(args, collections.Hashable):
			return self.func(*args)
		if args in self.cache:
			return self.cache[args]
		else:
			value = self.func(*args)
			self.cache[args] = value
			return value
	def __repr__(self):
		return self.func.__doc__
	def __get__(self, obj, objtype):
		return functools.partial(self.__call__, obj)

@memoized
def longestCommonSubstring (s, t):
	m = len(s)
	n = len(t)
	LCSuff = [[0 for x in xrange(n)] for x in xrange(m)] 
	z = 0
	for i in range (1, m):
		for j in range (1, n):
			if s[i] == t[j]:
				if i == 1 or j == 1:
					LCSuff[i][j] = 1
				else:
					LCSuff[i][j] = LCSuff[i-1][j-1] + 1
				if LCSuff[i][j] > z:
					z = LCSuff[i][j]
					indexS1 = i
					indexS2 = j
				else:
					if LCSuff[i][j] == z:
						indexS1 = i
						indexS2 = j
			else:
				LCSuff[i][j] = 0
	if z != 0:
		result = z + 1
		if (result == m):
			resultString = t[result:]
			return (result, resultString, -1, -1)
		if (result == n):
			return (result, "", -1, -1)
		if indexS2 > indexS1:
			resultString = t[:indexS2-z] 
			return (result, resultString, indexS1, indexS2)
		else:
			resultString = t[indexS2+1:]
			return (result, resultString, indexS1, indexS2) 
	else:
		return (0, "", -2, -2)

DNAvisited = {}
def DNAsequencing(substrings):
	finalStringToAppend = ""
	biggestString = ""
	biggestOverlapLength = 0
	maxl = 0
	for s in substrings:
		if len(s) > maxl:
			maxl = len(s)
			currString = s
	DNAvisited[currString] = True
	biggestOverlapIndex = None
	usedStrings = []
	usedStrings.append(currString)
	i = 0
	while i < len(substrings) :
		j = 0
		while j < len(substrings) :
			substringJ = substrings[j]
			if DNAvisited[substringJ] == False:
				if substringJ in currString:
					DNAvisited[substringJ] = True
				else: 
					for s in usedStrings:
						result = longestCommonSubstring(s, substringJ)
						currOverlapLength= result[0]
						stringToAppend = result[1]		
						if (((currOverlapLength == biggestOverlapLength) & (len(substringJ) > len(biggestString))) | (currOverlapLength > biggestOverlapLength)):
							finalStringToAppend = stringToAppend
							biggestOverlapLength = currOverlapLength
							biggestString = substrings[j]
							biggestIndexS1 = result[2]
							biggestIndexS2 = result[3]
			j+=1
		if (biggestIndexS2 == -1):
			currString = currString + finalStringToAppend
		if (biggestIndexS2 > biggestIndexS1 & biggestIndexS1 != -1 & biggestIndexS2 != -1):
			currString = finalStringToAppend + currString
		else:
			if (biggestIndexS1 != -1 & biggestIndexS2 != -1):
				currString = currString + finalStringToAppend
		DNAvisited[biggestString] = True
		usedStrings.append(biggestString)
		biggestOverlapLength = 0
		finalStringToAppend = ""
		biggestIndexS1 = -1
		biggestIndexS2 = -1
		i+=1
	print  "L:   " + currString
	return currString

textFiles = ['reads1.txt', 'reads2.txt', 'reads3.txt', 'reads4.txt', 'reads5.txt', 'reads6.txt', 'reads7.txt' ,'reads8.txt' , 'reads9.txt', 'reads10.txt', 'reads11.txt']
textFilesFirstFiveAnswers = ['answer1.txt', 'answer2.txt', 'answer3.txt', 'answer4.txt', 'answer5.txt']
textFilesFirstTen = ['reads1.txt', 'reads2.txt', 'reads3.txt', 'reads4.txt', 'reads5.txt', 'reads6.txt', 'reads7.txt' ,'reads8.txt' , 'reads9.txt', 'reads10.txt']
very_start_time = time.clock()
textFilesLast = ['reads12.txt', 'reads13.txt', 'reads15.txt', 'reads16.txt']
textFilesLastTwo = ['reads11.txt', 'reads14.txt']

i = -1
for txt in textFilesLast:
	f = open(txt, 'r')
	substrings = []
	for line in f:
		substrings.append(line.rstrip('\n'))
		DNAvisited[line.rstrip('\n')] = False
	start_time = time.clock()
	DNAsequencing(substrings)
	end_time = time.clock() - start_time
	"""if (i < 4):
		i += 1
		ans = open(textFilesFirstFiveAnswers[i], 'r')
		print "A:   " + ans.read()
	
	"""
	print str(txt) + " finished in", end_time, "seconds"
	substrings = []
print "total time is ", time.clock() - very_start_time, "seconds"
