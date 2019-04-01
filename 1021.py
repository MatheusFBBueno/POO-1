# -*- coding: utf-8 -*-
v = float(input())

if 0 <= v <= 1000000.00:
	print("NOTAS:")
	a = v // 100
	print("%.d nota(s) de R$ 100.00" % a)
	H = v % 100
	b = H // 50
	print("%d nota(s) de R$ 50.00" % b)
	I = H % 50
	c = I // 20
	print("%d nota(s) de R$ 20.00" % c)
	J = I % 20
	d = J //10
	print("%d nota(s) de R$ 10.00" % d)
	K = J % 10
	e = K // 5
	print("%d nota(s) de R$ 5.00" % e)
	L = K % 5
	f = L //2
	print("%d nota(s) de R$ 2.00" % f)
	print("MOEDAS:")
	M = L % 2
	g = M // 1
	print("%d moeda(s) de R$ 1.00" % g)
	N = M % 1
	h = N // 0.50
	print("%d moeda(s) de R$ 0.50" % h)
	O = N % 0.50
	i = O // 0.25
	print("%d moeda(s) de R$ 0.25" % i)
	P = O % 0.25
	j = P // 0.10
	print("%d moeda(s) de R$ 0.10" % j)
	Q = P % 0.10
	k = Q // 0.05
	print("%d moeda(s) de R$ 0.05" % k)
	R = Q % 0.05
	l = (R * 100)
	print("%d moeda(s) de R$ 0.01" % round(l))