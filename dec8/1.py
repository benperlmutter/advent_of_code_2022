#dec8 1

def vTree(char, s):
	# print("this is s {}".format(s))	
	# print("this is char {}".format(char))
	# print(s)
	if len(s) < 1:
		return True
	elif len(s) < 2:
		# print(int(char) > int(s))
		return int(char) > int(s)
	else:
		if int(char) > int(s[0]):
			return vTree(char, s[1:])
		else:
			return False


def visibleTree(s, i):
	aSide = True
	bSide = True
	num = s[i]
	print(s)
	for char in s[:i]:
		# print("num is {}".format(num))
		if num <= char:
			print("numb is {} and i is {} and s is {}".format(num,i,s[:i]))
			aSide = False
	for char in s[i+1:]:
		print("numb is {} and i is {} and s is {}".format(num,i,s[i+1:]))
		if num <= char:
			bSide = False
	if aSide or bSide:
		return True
	else:
		return False


file1 = open('sample_input.txt', 'r')
# file1 = open('input.txt', 'r')
lines = file1.readlines()

rows = []
columns = {}
visibleTrees = []

row1 = 0

for line in lines:
	# print(line)
	columnIter = 0
	rows.append(line.split('\n')[0])
	if row1 == 0:
		for char in line:
			if char != '\n':
				columns[columnIter] = char
				columnIter += 1
		row1 += 1
	else:
		for char in line:
			if char != '\n':
				columns[columnIter] += char
				columnIter += 1

print(rows)
rowIter = 1
rowSize = len(rows)

for r in rows:
	charRowIter = 0
	for char in r:
		if rowIter == 1 or rowIter == rowSize:
			visibleTrees.append([char,charRowIter,r])
		else:
			# print(char)
			t1 = vTree(char,r[:charRowIter])
			t2 = vTree(char,r[charRowIter+1:])
			print(rowIter)
			print("column {} and cNum {}".format(columns[charRowIter],columns[charRowIter][rowIter-1]))
			if t1 or t2:
				visibleTrees.append([char,charRowIter,r])
				print("appended {}".format(char))
		charRowIter += 1
	rowIter += 1


for x in visibleTrees:
	print(x)
	
print(len(visibleTrees))	


# print(visibleTrees)
print(columns)

# for r in rows:
# 	i = 0
# 	for n in r:
# 		if visibleTree(r, i) and i != 0:
# 			# print("index {} char {} in row {} is visible".format(i,n,r))
# 			print("appending {}".format(n))
# 			visibleTrees.append([i,n,r])
# 			# print('break')
# 			# print(visibleTrees)
# 		i += 1

# for key, value in columns.items():
# 	# print(value)
# 	i = 0
# 	for n in value:
# 		if visibleTree(value, i) and i != 0:
# 			# print("index {} char {} in row {} is visible".format(i,n,r))
# 			print("appending {}".format(n))
# 			visibleTrees.append([i,n,value])
# 			# print('break')
# 		i += 1

# for i in visibleTrees:
# 	print(i)
# print(len(visibleTrees))



