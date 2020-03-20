# Pregunta 2 entrevista Tomas Burotto


class Route:
    # La clase ruta recibe 2 atributos tipo string y multiples atributos de la clase Guide (relacion 1:N) con clase
    # Guide
    def __init__(self, date, truck_identifier, *guides):
        self.date = date
        self.truck_identifier = truck_identifier
        # Alamacenamos los Guides en un array
        self.guides = []
        for guide in guides:
            self.guides.append(guide)
    # Esta funcion solo permite printear informacion cuando se llama al metodo print de la clase Route

    def __repr__(self):
        return "Date: {0}, Truck_id: {1}, Guides: {2}".format(self.date, self.truck_identifier, self.guides)


class Guide:
    # La clase Guide recibe 3 atributos todos de tipo string
    def __init__(self, identifier, contact_name, contact_adress):
        self.identifier = identifier
        self.contact_name = contact_name
        self.contact_adress = contact_adress

    # Esta funcion solo permite printear informacion cuando se llama al metodo print de la clase Guide
    def __repr__(self):
        return self.contact_name


if __name__ == "__main__":

    guide1 = Guide(1, "Alfredo", "Alameda 123")
    guide2 = Guide(2, "Luis", "Alameda 123")
    guide3 = Guide(3, "Juan", "Alameda 123")
    guide4 = Guide(4, "Clara", "Alameda 123")
    route1 = Route("28-01-20", "abcd12", guide1, guide2, guide3)
    print(route1)
