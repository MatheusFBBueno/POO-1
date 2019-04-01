x = int(input())
y = int(input())
s = 0

if x> y:
	b = x
	x = y
	y = b
if x % 2 != 0:
	x += 2
	while(x < y):
		if x % 2 != 0:
			s += x
		x += 1
else:
	x += 1
	while (x < y) :
		if x % 2 != 0:
			s += x
		x += 1
print(s)