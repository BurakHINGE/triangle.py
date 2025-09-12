while True:
	def ucgen():

		a = int(input("En az 2 olacak şekilde üçgenin büyüklüğünü yazınız: "))

		if a<2:
			print("2 veya daha büyük bir sayı giriniz: ")

		else:
			for i in range(1,a+1,1):
				for k in range(i):
					print("*", end = " ")
				print()		
	ucgen()
