# -*- coding: utf-8 -*-

class BitcoinExchange:

    __BTC_price = 0
    __USD = 0

    def __init__(self, BTC, USD):
        self.set_values(BTC, USD)

    def set_values(self, BTC, USD):
        self.__BTC_price = BTC
        self.__USD = USD

    def get_BTC_price(self):
        return self.__BTC_price

    def get_USD(self):
        return self.__USD

    def __str__(self):
        return f"You can buy {self.bitcoin_exchange_value()} BTC"


    def bitcoin_exchange_value(self):
        result = self.get_USD() / self.get_BTC_price()
        return round(result, 7)

def main_program():
    BTC_price = float(input("What is Bitcoin price today?\n"))
    USD = float(input("How much $ do you have?\n"))
    if BTC_price <= 0:
        raise TypeError('Bitcoin price must be greater than zero')
    elif USD <= 0:
        raise TypeError('Dollars price must be greater than zero')
    else:
        print(BitcoinExchange(BTC=BTC_price, USD=USD))

if __name__ == '__main__':
    try:
        main_program()
    except ValueError:
        print("Please enter a number!")
        exit(1)


