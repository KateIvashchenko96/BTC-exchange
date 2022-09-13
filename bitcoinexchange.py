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
        result = int(self.get_USD()) / int(self.get_BTC_price())
        return round(result, 7)

if __name__ == '__main__':

    BTC_price = float(input("What is Bitcoin price today?\n"))
    USD = float(input("How much $ do you have?\n"))
    print(BitcoinExchange(BTC=BTC_price, USD=USD))


