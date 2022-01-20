print("Feladat 1053")
print("bekért Karakterek magánhangzóinak száma")

karlanc = input("Karakterlánc: ")
magan = ['a','á','e','é','i','í','o','ó','ü','ű','ö','ő']
darab = 0
for kar in karlanc:
	if kar in magan:
		darab += 1

print("A magánhangzók száma: ", darab)
