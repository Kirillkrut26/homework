from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def price(self) -> float:
        pass


class Product(BaseProduct):
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
        super().__init__()

    @classmethod
    def new_product(cls, dict_products: dict) -> Product:
        name_dict = dict_products["name"]
        description_dict = dict_products["description"]
        price_dict = dict_products["price"]
        quantity_dict = dict_products["quantity"]
        return cls(name_dict, description_dict, price_dict, quantity_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError


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
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{product}\n"

        return result

    @property
    def products_in_list(self):
        return self.__products

    def summ_product_category(self):
        category_quantity = 0
        for product in self.__products:
            category_quantity += product.quantity

        return category_quantity

    def __str__(self):
        return (
            f"{self.name}, количество продуктов: " f"{self.summ_product_category()} шт."
        )


class CategoryIterator:

    def __init__(self, category: Category) -> None:
        self.category = category
        self.index = 0

    def __iter__(self) -> CategoryIterator:
        self.index = 0
        return self

    def __next__(self) -> Product:
        if self.index < len(self.category.products_in_list):
            product = self.category.products_in_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


class PrintMixin:
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', '{self.description}', {self.price}, {self.quantity})"


class Smartphone(Product, PrintMixin):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product, PrintMixin):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
