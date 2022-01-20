szoveg = input('Karaktersorozat: ')
hossz = len(szoveg)
for i in range(0, hossz):
	print(szoveg[i])
	for j in range(-1, i):
		print(' ', end='')
