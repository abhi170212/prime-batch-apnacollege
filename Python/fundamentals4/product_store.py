class OnlineShop:
    store_name = "AKS Sports"
    total_products = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        OnlineShop.total_products += 1  # yahan pehle error tha

    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (price * discount / 100)
        print(f"The final price of the item is {final_price}")

    @classmethod
    def get_total_products(cls):
        print(f"Total products are: {cls.total_products} and store name is:  {cls.store_name}")


l1 = OnlineShop("Football Jersey", 1000)
l2 = OnlineShop("Football Shoes", 2000)
l3 = OnlineShop("GK Gloves", 3200)
OnlineShop.get_total_products()
l1.calc_discount(1000, 5)
OnlineShop.get_total_products()
