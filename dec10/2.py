#dec10 2

# file1 = open('sample_input.txt', 'r')
file1 = open('input.txt', 'r')
lines = file1.readlines()

c = 0
x = 1
total = 0

gridSize = 40

a = []
b = []

p=""

for line in lines:
	l = line.split()
	a.append(l)

for i in range(len(a)):
	b.append(a.pop())

count = 0
# z = len(b)
# for el in range(z):
# 	print(el)
# 	l = b.pop()
# 	# print(len(l))
# 	if len(l) < 2:
# 		count += 1
# 	else:
# 		count += 2

# print(count)

while len(b) > 0:
	# print(el)
	# print('this is length of b {}'.format(len(b)))
	flag = False
	while (len(p) < gridSize) and (len(b) > 0):
		l = b.pop()
		# print(l[0])
		if len(l) <2:
			# count += 1
			# print("start cycle {}".format(len(p)))
			# print("x is {}".format(x))
			if (x == len(p)) or (x-1 == len(p)) or (x+1 == len(p)):
				p += "#"
				count += 1
			else:
				p += "."
				count += 1

		else:
			# count += 2
			# print("start cycle {}".format(c))
			# print("x is {}".format(x))
			if (x == len(p)) or (x-1 == len(p)) or (x+1 == len(p)):
				p += "#"
				count += 1
			else:
				p += "."
				count += 1

			# print(x)
			# print("cycle is {}".format(c))
			# print(p)
			
			# print("start cycle {}".format(c))
			if len(p) < gridSize:
				if (x == len(p)) or (x-1 == len(p)) or (x+1 == len(p)):
					p += "#"
					count += 1
				else:
					p += "."
					count += 1
			else:
				flag = True


				# print(x)
				# print("cycle is {}".format(c))
				# print(p)

			if flag == False:
				x += int(l[1])
			# print(x)

		# print(c)
	print(p)
	# x = 1
	p = ""
	if flag:
		if (x == len(p)) or (x-1 == len(p)) or (x+1 == len(p)):
			p += "#"
			count += 1
		else:
			p += "."
			count += 1
		x += int(l[1])


print(count)

# print(b)
# print(b.pop())