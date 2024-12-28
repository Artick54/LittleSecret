
init 22 python:

    class Love(object): # Crear variable de amor y tener limites
        def __init__(self, name, quantity, quantity_max):
            self.name = name
            self.quantity = quantity
            self.quantity_max = quantity_max

        def add_love(self, quantity, random=False, max_=20):
            if quantity < 0:
                raise ValueError("The amount must be positive.") # La cantidad no debe ser negativo (Ej: -1, -2, ect...)
            if random == False:
                self.quantity += quantity
            else:
                quantity += renpy.random.randint(1, max_)
                self.quantity += quantity

            if self.quantity > self.quantity_max:
                self.quantity = self.quantity_max

            print(f"❤️Add>>>", quantity) #Solo se muestra en la consola

        def get_quantity(self):
            return self.quantity #Solo se muestra en la consola
    
        def remove_love(self, quantity, random=False, max_=10):
            if quantity < 0:
                raise ValueError("The amount must be positive.")
            if self.quantity >= quantity:
                if random == False:
                    self.quantity -= quantity
                else:
                    quantity += renpy.random.randint(1, max_)
                    self.quantity -= quantity
            else:
                self.quantity = 0

            print(f"💔Remove>>>", -quantity) #Solo se muestra en la consola

        def __str__(self):
            return f"{self.quantity}/{self.quantity_max}"
