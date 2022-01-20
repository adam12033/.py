def have_dog(kutya):
	fajtak = ['dalmata', 'agár', 'terrier' ,'kuvasz']
	if kutya in fajtak:
		return "Van ilyen fajta"
	else:
		return "Jelenleg nincs ilyen fajta"

kutya = ''
while kutya != 'vege':
	kutya = input('Kutya neve: ')
	if kutya != 'vege':
		uzenet = have_dog(kutya)
		print(uzenet)
