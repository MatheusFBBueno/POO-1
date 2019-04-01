a,b = input().split()
a = int(a)
b = int(b)
while(a != 0 and b != 0):
	
	if a >  0 and b > 0:
		print("primeiro")
		a,b = input().split()
		a = int(a)
		b = int(b)
	elif a < 0 and b > 0:
		print("segundo")
		a,b = input().split()
		a = int(a)
		b = int(b)
	elif a < 0 and b < 0:
		print("terceiro")
		a,b = input().split()
		a = int(a)
		b = int(b)
	elif a > 0 and b < 0:
		print("quarto")
		a,b = input().split()
		a = int(a)
		b = int(b)
	elif a == 0 or b == 0:
		break
