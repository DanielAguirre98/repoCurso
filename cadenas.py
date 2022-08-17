class Auto:
    def __init__(self, marca, modelo, año, km):
        self.marca=marca
        self.modelo=modelo
        self.año=año
        self.km=km

    def __str__(self):
        return f"Marca: {self.marca}, modelo: {self.modelo}, año: {self.año} con un kilometraje de {self.km}"

    def prenderLuces(self, estado):
        self.estado=estado
        if estado=="Prender":
            print(f"Prendi las luces de mi {auto1}")
        else:
            print("El auto se encuentra apagado")
posta="aloja.py"

comit="comit2"
aloja="perri"
            

        

auto1=Auto("Renault", "clio", 2016, 98.000)
auto1.prenderLuces("Prender")
print(auto1)


class Fallado:
    def __init__(self, codigo, prenda, talle):
        self.codigo=codigo
        self.prenda=prenda  
        self.talle=talle
    
    def __str__(self):
        return f"""CODIGO: {self.codigo}
        PRENDA: {self.prenda}
        TALLE: {self.talle}"""

prenda1=Fallado("22N3219", "TRAXU", "32")

print(prenda1)