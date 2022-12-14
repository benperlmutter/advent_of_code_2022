#dec9 1

# file1 = open('sample_input.txt', 'r')
file1 = open('input.txt', 'r')
lines = file1.readlines()

def moveRope(coord, direction, num, h, t, moveDict):
	for i in range(num):
		# print(moveDict)
		if coord == "x":
			if direction == "add":
				h[0] += 1
				if abs(h[0] - t[0]) > 1:
					if abs(h[1] - t[1]) == 1:
						t[1] = h[1]
					t[0] += 1
					moveDict.setdefault(""+str(t[0])+","+str(t[1]), 0)
					moveDict[""+str(t[0])+","+str(t[1])] += 1

			else:
				h[0] -= 1
				if abs(h[0] - t[0]) > 1:
					if abs(h[1] - t[1]) == 1:
						t[1] = h[1]
					t[0] -= 1
					moveDict.setdefault(""+str(t[0])+","+str(t[1]), 0)
					moveDict[""+str(t[0])+","+str(t[1])] += 1

		else:
			if direction == "add":
				h[1] += 1
				if abs(h[1] - t[1]) > 1:
					if abs(h[0] - t[0]) == 1:
						t[0] = h[0]
					t[1] += 1
					moveDict.setdefault(""+str(t[0])+","+str(t[1]), 0)
					moveDict[""+str(t[0])+","+str(t[1])] += 1
			else:
				h[1] -= 1
				if abs(h[1] - t[1]) > 1:
					if abs(h[0] - t[0]) == 1:
						t[0] = h[0]
					t[1] -= 1
					moveDict.setdefault(""+str(t[0])+","+str(t[1]), 0)
					moveDict[""+str(t[0])+","+str(t[1])] += 1

def def_value():
	return 0


head = [0,0]
tail = [0,0]
moveDict = {"0,0": 1}

for line in lines:
	l = line.split(" ")
	direction = l[0]
	number = int(l[1])
	if direction == "R":
		# print("add to x coord")
		moveRope("x", "add", number, head, tail, moveDict)
	elif direction == "U":
		# print("add to y coord")
		moveRope("y", "add", number, head, tail, moveDict)
	elif direction == "D":
		# print("subtract from y coord")
		moveRope("y", "subtract", number, head, tail, moveDict)
	else:
		# print("subtract from x coord")
		moveRope("x", "subtract", number, head, tail, moveDict)

	# print(direction)
	# print(number)
print(moveDict)
print(len(moveDict))