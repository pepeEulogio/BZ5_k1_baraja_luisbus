from random import shuffle

class Baraja:

	def __init__ (self):
		self.__espadas=["E01","E02","E03","0E4","E05","E06","E07","E10","E11","E12"]
		self.__oros=["O01","O02","O03","O04","O05","O06","O07","O10","O11","O12"]
		self.__copas=["C01","C02","C03","C04","C05","C06","C07","C10","C11","C12"]
		self.__bastos=["B01","B02","B03","B04","B05","B06","B07","B10","B11","B12"]
		self.__cartas=[self.__espadas,self.__copas,self.__oros,self.__bastos]
		self.__jugadores=0
		self.__nCartas=0
		#print(self.__cartas)

	def barajear (self):
		self.barajeado=[]
		for i in self.__cartas:
			for j in i:
				self.barajeado.append(j)			
		shuffle(self.barajeado)
		print(self.barajeado)
		#print(random.choice(random.choice(self.__cartas)))

	def repartir (self, jugadores, cartas):
		self.__jugadores=jugadores
		self.__nCartas=cartas
		cont=0
		for i in range(self.__jugadores):
			jugador=[]
			cont+=1
			for j in range(self.__nCartas):
				jugador.append(self.barajeado[0])
				for i in jugador:		
					if i in self.barajeado:
						self.barajeado.remove(i)

			print("Cartas jugador ", str(cont), " :", jugador)

	def recoger_colocar (self):
		#self.recoger_colocar=sorted(self.barajeado)
		#print(self.recoger_colocar)
		self.barajeado.sort()
		print(self.barajeado)
		

baraja1=Baraja()
baraja1.barajear()
print("-------------------------------------------------------------------------")
baraja1.repartir(5,6)
print("-------------------------------------------------------------------------")
baraja1.recoger_colocar()
