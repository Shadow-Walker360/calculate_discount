# Discount Calculator

This is a simple Python program that calculates the final price of an item after applying a discount. The function `calculate_discount(price, discount_percent)` takes the original price and a discount percentage as input parameters. If the discount is 20% or higher, the discount is applied; otherwise, the original price is returned.

## Features

- Prompts the user for the original price and discount percentage.
- Applies the discount only if it is 20% or greater.
- Displays the final price after discount or indicates that no discount was applied.

## Requirements

- Python 3.x

## How to Run

1. Clone or download the repository.
2. Open a terminal and navigate to the project directory.
3. Run the program using the following command:
    ```bash
    python discount_calculator.py
    ```
4. Follow the on-screen prompts to enter the original price and discount percentage.

## Code Explanation

- **Function:** `calculate_discount(price, discount_percent)`
  - **Parameters:** 
    - `price`: The original price of the item.
    - `discount_percent`: The discount percentage to apply.
  - **Behavior:** If the discount percentage is 20 or more, it calculates and returns the discounted price. Otherwise, it returns the original price.
- **Main Function:** Handles user input, calls `calculate_discount`, and prints the appropriate final price.

## Example

- If the user enters an original price of $100 and a discount of 25%, the final price will be calculated as $75.
- If the discount percentage is less than 20, the program will inform the user that no discount was applied and display the original price.


