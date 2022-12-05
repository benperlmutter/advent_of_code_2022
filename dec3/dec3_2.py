#dec1 1

file1 = open('input.txt', 'r')
lines = file1.readlines()

abc_s = "abcdefghijklmnopqrstuvwxyz"

scoreDict = {}
dict1 = {}
for char in range(len(abc_s)):
	scoreDict[abc_s[char]] = char+1
	dict1[abc_s[char]] = 0
	dict1[abc_s[char].upper()] = 0
	# print(scoreDict)

count = 0
thisScore = 0
setC = 1

for line in lines:
	thisLine = line.strip()
	if setC % 3 == 1:
		for char in thisLine:
			dict1[char] = 1
	elif setC % 3 == 2:
		for char in thisLine:
			if dict1.get(char) == True:
				dict1[char] += 1
				# print(dict1[char])
	elif setC % 3 == 0:
		print(thisLine)
		for char in thisLine:
			# print("current set is {} and dict looks like {}".format(setC, dict1))
			print(dict1.get("r") == True)

			if dict1[char] > 1:
				# print(char)
				# print("the CHAR {}".format(char))

				if dict1[char] > 1:
					shared = char
					count += scoreDict[shared.lower()]
					thisScore = scoreDict[shared.lower()]
					if shared == shared.upper():
						count += 26 
						thisScore += 26
					for char in range(len(abc_s)):
						dict1[abc_s[char]] = 0
						dict1[abc_s[char].upper()] = 0
				# print("count is {}".format(count))
				# print(thisScore)
	# print("current set is {} and dict looks like {}".format(setC, dict1))

	setC += 1

print(count)





