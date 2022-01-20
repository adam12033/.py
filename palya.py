varosok =['Budapest', 'Miskolc' , 'Pécs' , 'Zalaegerszeg' ]
terulet = input("Város: ")

for varos in varosok:
	
	if ( varos == terulet ):
		oreg = int(input( "Öregedés: " ))
		if( oreg > 2 and oreg < 5 ):
			print("Felülvizsgálat!")
			
		if( oreg > 5 ):
			print( "Sürgős karbantartás!" )
		
		else:
			print( "Normal" )
