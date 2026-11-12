class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_products: dict) -> Product:
        name_dict = dict_products['name']
        description_dict= dict_products['description']
        price_dict= dict_products['price']
        quantity_dict= dict_products['quantity']
        return Product(name_dict, description_dict, price_dict, quantity_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('“Цена не должна быть нулевая или отрицательная”')
        else:
            self.__price = new_price


class Category:
    category_count: int = 0
    product_count: int = 0
    name: str
    description: str
    products: list[Product]

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count +=1

    @property
    def products(self):
        result = ''
        for product in self.__products:
            result += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'

        return result


