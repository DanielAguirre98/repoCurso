entradas=("Papas fritas", "Papas con cheddar", "Langostinos", "Bastones de muzarella", "Chicken fingers")
platos_principales=("La hemana de ale", "Fideos con bolognesa","Lazagna","Asadito", "Chorizo a la pomarola", "Rabas")
bebidas=("Agua sin gas", "Coca-cola","Fanta","Aquarios")



class pedido:
    def __init__(self, entrada, plato_principal,bebida):
        self.entrada=entrada
        self.plato_principal=plato_principal
        self.bebida=bebida
    
    def __str__(self):
        return f"Pedido: Entrada {self.entrada} ,Plato principal {self.plato_principal}, Bebida {self.bebida}"




print(pedido1)



