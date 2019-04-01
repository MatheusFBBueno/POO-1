# -*- coding: utf-8 -*-
s = float(input())

while s > 0:
	if s <= 400:
		r = (s * 1.15)
		d = (r - s)
		print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 15 %%" % (r, d))
	elif s <= 800:
		r = (s * 1.12)
		d = (r - s)
		print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 12 %%" % (r, d))
	elif s <= 1200:
		r = (s * 1.10)
		d = (r - s)
		print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 10 %%" % (r, d))
	elif s <= 2000:
		r = (s * 1.07)
		d = (r - s)
		print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 7 %%" % (r, d))
	else:
		r = (s * 1.04)
		d = (r - s)
		print("Novo salario: %.2f\nReajuste ganho: %.2f\nEm percentual: 4 %%" % (r, d))
	break