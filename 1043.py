# -*- coding: utf-8 -*-
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
p = (a + b + c)
A = ((a + b) * (c / 2))
if a < (b + c) and b < (a + c) and c < (b + a):
	print("Perimetro = %.1f" % p)
else:
	print("Area = %.1f" % A)
