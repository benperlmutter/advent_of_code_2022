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
for line in lines:
	for char in line:
		if (char1 not in char2+char3+char4) and (char2 not in char1+char3+char4) and (char3 not in char1+char2+char4) and (char4 not in char1+char2+char3):
			print("{}{}{}{} and counter is {}".format(char1,char2,char3,char4,counter-1))
		elif counter == 1:
			char1 = char
			counter += 1
		elif counter == 2:
			char2 = char
			counter += 1
		elif counter == 3:
			char3 = char
			counter += 1
		elif counter == 4:
			char4 = char
			counter += 1
		else:
			char1 = char2
			char2 = char3
			char3 = char4
			char4 = char
			counter += 1

