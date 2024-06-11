from libro import Libro
from revista import Revista
from estudiante import Estudiante
from docente import Docente

if __name__ == "__main__":
    libro1 = Libro(material_id=1, title="Python Programming", author="John Doe", year=2022)
    revista1 = Revista(material_id=2, title="Data Science Today", issue_number=5)
    estudiante1 = Estudiante(cedula="123456", nombre="Alice", apellido="Smith", email="alice@example.com", student_id="S123")
    docente1 = Docente(cedula="789012", nombre="Bob", apellido="Brown", email="bob@example.com", employee_id="E456")

    print(libro1)
    print(revista1)
    print(estudiante1)
    print(docente1)
