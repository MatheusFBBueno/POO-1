i = 0
o = 0
n = int(input())

for _ in range(0,n):
	x = int(input())

	if 10 <= x <= 20:
		i += 1
	else:
		o += 1
print("%d in" % i)
print("%d out"% o)