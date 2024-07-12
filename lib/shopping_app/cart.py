from item import Item

class Cart:
    from item_manager import show_items
    from ownable import set_owner

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def get_seller(self):
        return self.items[0].owner
    
    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print('Tu saldo es insuficiente')
        else:
            self.owner.wallet.withdraw(self.total_amount())
            self.get_seller().wallet.deposit(self.total_amount())
            for item in self.items:
                Item.instances.remove(item)    
            self.items = []



            
# Al codificar el método check_out, elimine la instrucción pass.
# Requisitos:
#   - El importe de compra de todos los artículos en el carrito (Cart#items) debe transferirse del monedero del propietario 
# del carrito al monedero del propietario de los artículos.
#   - La propiedad de todos los artículos en el carrito (Cart#items) debe transferirse al propietario del carrito.
#   - El carrito (Cart#items) debe quedar vacío.
# Pistas:
#   - El monedero del propietario del carrito ==> self.owner.wallet
#   - El monedero del propietario del artículo ==> item.owner.wallet
#   - Transferir dinero significa ==> retirar esa cantidad del monedero de (¿?) y depositar esa cantidad en el monedero de (¿?)
#   - Transferir la propiedad de los artículos al propietario del carrito ==> cambiar la propiedad (item.owner = ?)

