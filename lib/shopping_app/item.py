class Item:
    from ownable import set_owner
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        # Itemインスタンスの生成時、そのItemインスタンス(self)は、insntancesというクラス変数に格納されます。
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        # Al crear una instancia de Item, esa instancia de Item (self) se almacena en una variable de clase llamada instances.
        return Item.instances
