
def jo_zoldseg(nev):
	zoldsegek = ['cékla','vöröshagyma','karalábe']
	if nev in zoldsegek:
		return True
	else:
		return False

darab_jo = 0
nev = ''
while nev != 'vege':
	nev = input('Zöldség neve: ')
	if nev != 'vege':
		if jo_zoldseg(nev):
			print('OK')
			darab_jo += 1
		else:
			print('Nem megfelelő zöldség: ')
print('Jó zöldségek darabszáma',darab_jo)
	



