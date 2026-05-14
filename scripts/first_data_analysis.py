def main():
    customer_name = "Asha"
    customer_segment = "Regular"
    quantities = [2, 1, 3]
    prices = [4.50, 12.00, 2.25]

    total_items = sum(quantities)
    total_spend = sum(quantity * price for quantity, price in zip(quantities, prices))
    average_item_price = total_spend / total_items

    print("First Python Script for Data Analysis")
    print(f"Customer: {customer_name}")
    print(f"Segment: {customer_segment}")
    print(f"Items purchased: {total_items}")
    print(f"Total spend: ${total_spend:.2f}")
    print(f"Average price per item: ${average_item_price:.2f}")


if __name__ == "__main__":
    main()