zoldseg_nev = input("Zöldség neve: ")

if zoldseg_nev == " ":
	exit()

zoldsegek = ['cékla','vöröshagyma','karalábe']

if zoldseg_nev in zoldsegek:
	print('Rendben')
else:
	print('Nincs ilyen')
