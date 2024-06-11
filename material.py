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

# Crear una instancia de Material
mi_material = Material(material_id=1, title="Libro")

# Obtener el título
print(mi_material.title)  # Imprime "Libro"

# Cambiar el título
mi_material.title = "Artículo"
print(mi_material.title)  # Imprime "Artículo"
