nevek = 'Béla, Imre, Gábor, Aladár, Imre'

darab = nevek.count('Imre')
print('Darab: ', darab)

nev = 'Imre'
for karakter in nev:
	print('karakter: ', karakter)
	
hossz = len(nev)
for i in range(0 ,hossz):
	print('Karakter: ', nev[i])
