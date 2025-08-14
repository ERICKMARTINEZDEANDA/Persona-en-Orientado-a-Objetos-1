class Persona:
	#Constructor
	def __init__(self): #self es requerido para entrar a los metodos dentro de la clase
		self.edad=18 #atributos
		self.nombre="Juan"
		print("se ha creado a", self.nombre, "de", self.edad, "años")

	#metodos
	def hablar (self, palabras = "No tengo palabras"): #Se puede colocar un valor predeterminado
		print(self.nombre, ": ", palabras)

juan = Persona()
juan.hablar()
juan.hablar("hola, estoy hablando")

