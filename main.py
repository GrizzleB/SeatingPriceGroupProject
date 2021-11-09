import random
import numpy
from decimal import Decimal
from decimal import ROUND_HALF_UP

ROW_NUMBER = 6
COLUMN_NUMBER = 4


def display_title():
    print("-" * 45)
    print("Seating-Price Chart Program in Python")
    print()
    print("Created by: Zaid & Ryan")
    print("Created on: 11/09/2021")
    print("Description: The program is designed to")
    print("1 - Create an airplane seating-price chart")
    print("2 - Display the seating-price chart")
    print("3 - Find and display the highest seat-price")
    print("4 - Find and display the lowest seat-price")
    print("5 - Calculate the average price")
    print("6 - Find ALL seats (row and column) that have the lowest Price")
    print("7 - Find ALL seats (row and column) that have the highest Price")
    print("8 - Find a seat (row and column) based on the price entered by users - Extra Credit 5 points")
    print("-" * 45)


def create_seating_price_chart(row_number, col_number):
    chart = []
    for row in range(row_number):
        row_list = []
        for col in range(col_number):
            seat_price = random.randint(500, 1000)
            row_list.append(seat_price)
        chart.append(row_list)

    return chart


def display_seating_price_chart(chart):
    print()
    print("---------Display Seating Price Chart---------")
    print(f"There are {ROW_NUMBER} rows and {COLUMN_NUMBER} columns in the plane")
    print("")
    i = 0
    while i < len(chart):
        print(f"{chart[i]}")
        i += 1
    print("-" * 45)
    print()


def find_max_value(chart):
    return numpy.max(chart)  # package must be installed


def find_min_value(chart):
    return numpy.min(chart)  # package must be installed


def calculate_average_price(chart):
    return numpy.average(chart)  # package must be installed


def find_seats_with_price(chart, price):
    seat_list = []
    row_number = len(chart)
    column_number = len(chart[0])
    for row in range(row_number):
        for col in range(column_number):
            if chart[row][col] == price:
                seat = [row, col]
                seat_list.append(seat)
    return seat_list


def extra_credit(chart):
    while True:
        try:
            user_price = int(input("Enter a price between 500 and 1000: "))
            if 500 <= user_price <= 1000:
                user_seat = find_seats_with_price(chart, user_price)
                if not user_seat:
                    print(f"Cannot find a seat with the price {user_price}. Enter price again")
                else:
                    print()
                    print("-----Display seat list with entered price----")
                    return user_seat
            else:
                print("Please enter a valid number (between 500 and 1000)")
        except ValueError:
            print("Please enter a valid number (between 500 and 1000)")


def main():
    display_title()

    chart_2d = create_seating_price_chart(ROW_NUMBER, COLUMN_NUMBER)
    display_seating_price_chart(chart_2d)

    highest_price = find_max_value(chart_2d)
    print(f"The highest price is ${highest_price}")

    lowest_price = find_min_value(chart_2d)
    print(f"The lowest price is ${lowest_price}")

    average_price = Decimal(calculate_average_price(chart_2d))
    average_price = average_price.quantize(Decimal("1.00"), ROUND_HALF_UP)
    print(f"The average price is ${average_price}")

    print()
    print("-----Display seat list with lowest price-----")
    low_seat = find_seats_with_price(chart_2d, lowest_price)
    print(*low_seat, sep=" , ")
    print("-" * 45)

    print()
    print("-----Display seat list with highest price----")
    high_seat = find_seats_with_price(chart_2d, highest_price)
    print(*high_seat, sep=" , ")
    print("-" * 45)

    print()
    found_seat = extra_credit(chart_2d)
    print(*found_seat, sep=" , ")
    print("-" * 45)


if __name__ == '__main__':
    main()
