# -*- coding: utf-8 -*-
v = int(input())

if 0 < v < 1000000:
	print("%d" % v)
	a = v // 100
	print("%d nota(s) de R$ 100,00" % a)
	h = v % 100
	b = h // 50
	print("%d nota(s) de R$ 50,00" % b)
	i = h % 50
	c = i // 20
	print("%d nota(s) de R$ 20,00" % c)
	j = i % 20
	d = j //10
	print("%d nota(s) de R$ 10,00" % d)
	k = j % 10
	e = k // 5
	print("%d nota(s) de R$ 5,00" % e)
	l = k % 5
	f = l //2
	print("%d nota(s) de R$ 2,00" % f)
	g = l % 2
	print("%d nota(s) de R$ 1,00" % g)