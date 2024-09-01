#!/usr/bin/env python3


def calculate_discount(price, discount_percent):
    """Takes in price, and multiplies it by dicount"""
    if (discount_percent >= 0.2):
        return price * discount_percent

    else:
        return price
    
inputed_price = int(input('Please input the price of the product: '))
discount = int(input("Please input the discount as a percentage: ")) / 100


total_discount = calculate_discount(inputed_price, discount)

newPrice = inputed_price - total_discount
print("New price is: ", newPrice)