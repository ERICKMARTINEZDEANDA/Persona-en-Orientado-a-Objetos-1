class Persona:
	#Constructor
	def __init__(self, edad, nombre): #self es requerido para entrar a los metodos dentro de la clase
		self.edad=edad #atributos
		self.nombre=nombre
		print("se ha creado a", self.nombre, "de", self.edad, "años")

	#metodos
	def hablar (self, palabras = "No tengo palabras"): #Se puede colocar un valor predeterminado
		print(self.nombre, ": ", palabras)

juan = Persona(18, "Juan")
juan.hablar()
juan.hablar("hola, estoy hablando")

