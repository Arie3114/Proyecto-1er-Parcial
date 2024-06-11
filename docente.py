from persona import Persona

class Docente(Persona):
    def __init__(self, cedula, nombre, apellido, email, employee_id):
        super().__init__(cedula, nombre, apellido, email)
        self.employee_id = employee_id

    @property
    def employee_id(self):
        return self._employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id

    def __str__(self):
        return f"Docente: {super().__str__()}, Employee ID: {self.employee_id}"

if __name__ == '__main__':
    d1 = Docente("987654", "Carlos", "González", "carlos@example.com", "D123")
    print(d1)
