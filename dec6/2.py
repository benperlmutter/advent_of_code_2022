#dec1 1

# file1 = open('sample_input.txt', 'r')
file1 = open('input.txt', 'r')
lines = file1.readlines()

charIndex = 1
char1 = ""
char2 = ""
char3 = ""
char4 = ""
counter = 1
finalCounter = 0
finalStr = ""
for line in lines:
	counter = 1
	charStr = ""
	firstTime = True
	for char in line:
		if counter <= 14:
			charStr += char
		else:
			charStr = charStr[1:]+char
			# print("{} is {}".format(counter, charStr))

		if len(charStr) == 14:
			dict1 = {}
			flag = True
			for c in charStr:
				if dict1.get(c):
					dict1[c] += 1
				else:
					dict1[c] = 1
			for c in charStr:
				if dict1[c] > 1:
					flag = False
			if flag and firstTime:
				print('in here')
				finalCounter = counter
				finalStr = charStr
				firstTime = False

		counter+=1
				# print("we have a winner at {}".format(counter))
	print("we have a winner with {} at {}".format(finalStr, finalCounter))




		# dict1 = {}
		# for c in charStr:


		

