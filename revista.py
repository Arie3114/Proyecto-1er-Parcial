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

class Revista(Material):
    def __init__(self, material_id, title, issue_number):
        super().__init__(material_id, title)
        self.issue_number = issue_number

    @property
    def issue_number(self):
        return self._issue_number

    @issue_number.setter
    def issue_number(self, new_issue_number):
        self._issue_number = new_issue_number

    def __str__(self):
        return f"Revista: {super().__str__()}, Issue Number: {self.issue_number}"

# Crear una instancia de Revista
mi_revista = Revista(material_id=3, title="Revista X", issue_number=10)

# Obtener información de la revista
print(mi_revista)  # Imprime "Revista: Material ID: 3, Title: Revista X, Issue Number: 10"
