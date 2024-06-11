class Material:
    def __init__(self, material_id, title):
        self.material_id = material_id
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        self._title = new_title

class Libro(Material):
    def __init__(self, material_id, title, author, year):
        super().__init__(material_id, title)
        self.author = author
        self.year = year

    def __str__(self):
        return f"Libro: {super().__str__()}, Author: {self.author}, Year: {self.year}"

# Crear una instancia de Libro
mi_libro = Libro(material_id=2, title="Novela", author="Autor X", year=2022)

# Obtener información del libro
print(mi_libro)  # Imprime "Libro: Material ID: 2, Title: Novela, Author: Autor X, Year: 2022"
