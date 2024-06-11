from persona import Persona

class Estudiante(Persona):
    def __init__(self, cedula, nombre, apellido, email, student_id):
        super().__init__(cedula, nombre, apellido, email)
        self.student_id = student_id

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        self._student_id = student_id

    def __str__(self):
        return f"Estudiante: {super().__str__()}, Student ID: {self.student_id}"

if __name__ == '__main__':
    e1 = Estudiante("123456", "Ana", "García", "ana@example.com", "S12345")
    print(e1)
