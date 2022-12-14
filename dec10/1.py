#dec9 1






# file1 = open('sample_input.txt', 'r')
file1 = open('input.txt', 'r')
lines = file1.readlines()

cycle = 0
x = 1
total = 0

cycles = [20,60,100,140,180,220]

for line in lines:
	l = line.split()
	# print(l)
	if len(l) <2:
		cycle +=1
		if cycle in cycles:
			print("cycle is {} and x is {} and combo is {}".format(cycle,x,cycle*x))
			total += cycle*x

	else:
		cycle += 1
		if cycle in cycles:
			print("cycle is {} and x is {} and combo is {}".format(cycle,x,cycle*x))
			total += cycle*x

		
		cycle += 1
		if cycle in cycles:
			print("cycle is {} and x is {} and combo is {}".format(cycle,x,cycle*x))
			total += cycle*x

		x += int(l[1])

print(total)