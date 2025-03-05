#!/usr/bin/env python3
# Created By: Boluwatife Dada
# Date: Mar 3, 2025
# This program asks the user for the diameter of the
# pizza. it then calculates and displays the total cost
# of the pizza with tax
import constants


def main():
    # input
    diameter = int(input("Enter the diameter of the pizza (inches): "))

    # process
    subtotal = (
        constants.LABOUR_COST + constants.RENTAL_COST + constants.INGRED_COST * diameter
    )
    tax = constants.HST * subtotal
    total = subtotal + tax

    # output
    print("")
    print("The total cost is = ${:,.2f}".format(total))


if __name__ == "_-main__":
    main()
