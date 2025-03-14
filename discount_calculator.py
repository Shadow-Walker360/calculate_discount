def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying the discount.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to apply.
    
    Returns:
        float: The final price after discount if discount_percent is 20 or higher;
               otherwise, returns the original price.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

def main():
    while True:
        user_input = input("Enter the original price of the item (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting the program.")
            break
        
        try:
            original_price = float(user_input)
        except ValueError:
            print("Invalid price input. Please enter a numeric value.")
            continue

        discount_input = input("Enter the discount percentage: ")
        try:
            discount_percent = float(discount_input)
        except ValueError:
            print("Invalid discount input. Please enter a numeric value.")
            continue

        final_price = calculate_discount(original_price, discount_percent)
        
        if discount_percent >= 20:
            print(f"The final price after applying a {discount_percent}% discount is: ${final_price:.2f}")
        else:
            print("No discount was applied.")
            print(f"The original price remains: ${final_price:.2f}")

        # Ask the user if they want to calculate another discount
        choice = input("Do you want to calculate another discount? (y/n): ")
        if choice.lower() != 'y':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
