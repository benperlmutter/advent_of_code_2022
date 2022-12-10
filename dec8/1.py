#dec9 1

file1 = open('sample_input.txt', 'r')
# file1 = open('input.txt', 'r')
lines = file1.readlines()

def inRange(x,y):
	if abs(x-y) <= 1:
		return True
	else:
		return False

x = 7
y = 8

print(inRange(x,y))