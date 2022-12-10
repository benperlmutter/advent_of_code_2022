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


# file1 = open('sample_input.txt', 'r')
file1 = open('input.txt', 'r')
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
rowIter = 0
rowSize = len(rows)

for r in rows: 
	for columnIter in columns:
		print(r[columnIter])
		print("the 4 pieces are \n{}\n{}\n{}\n{}\n".format(columns[columnIter][:rowIter], columns[columnIter][rowIter+1:], r[:columnIter], r[columnIter+1:]))
		t1 = vTree(r[columnIter],columns[columnIter][:rowIter])
		t2 = vTree(r[columnIter],columns[columnIter][rowIter+1:])
		t3 = vTree(r[columnIter],r[:columnIter])
		t4 = vTree(r[columnIter],r[columnIter+1:])
		if t1 or t2 or t3 or t4:
			visibleTrees.append(r[columnIter])
		print('\n')
	rowIter += 1


for x in visibleTrees:
	print(x)
	
print(len(visibleTrees))	

print(columns)

