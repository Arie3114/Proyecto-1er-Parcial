class Persona:
    def __init__(self, cedula, nombre, apellido, email):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self):
        return f"Persona: Cedula: {self.cedula}, Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}"

if __name__ == '__main__':
    p1 = Persona("123456", "Juan", "Pérez", "juan@example.com")
    print(p1)
