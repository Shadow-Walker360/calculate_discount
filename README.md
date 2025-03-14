# Discount Calculator with Loop Control

This Python program calculates the final price of an item after applying a discount, using a control structure (while loop) to allow multiple calculations. The function `calculate_discount(price, discount_percent)` takes the original price and discount percentage as input. A discount is applied only if it is 20% or higher; otherwise, the original price is returned.

## Features

- **Loop Control:** Continuously prompts the user for new calculations until they choose to exit.
- **Breakpoints:** Uses break statements to exit the loop when the user types "exit" or when they decide not to perform another calculation.
- **Input Validation:** Ensures that valid numeric inputs are provided; if not, it prompts the user again.

## Requirements

- Python 3.x

## How to Run

1. Clone or download the repository.
2. Open a terminal and navigate to the project directory.
3. Run the program using:
    ```bash
    python discount_calculator.py
    ```
4. Follow the on-screen prompts to enter the original price and discount percentage.
5. Type "exit" at the price prompt or choose not to continue when asked if you want to calculate another discount.

## Code Explanation

- **Function:** `calculate_discount(price, discount_percent)`
  - Applies the discount only if the discount percentage is 20 or more.
- **Main Loop:**
  - Uses a `while True` loop to continuously prompt the user.
  - The user can exit by typing "exit" or by indicating they do not wish to perform another calculation.
  - Input is validated to ensure proper numeric values.
