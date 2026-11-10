

def main():
    print("--- Number Converter ---")
    user_input = input("Enter a positive decimal number: ")
    
    decimal_num = int(user_input)
    
    binary_val = bin(decimal_num)
    hex_val = hex(decimal_num)
    
    print(f"Decimal: {decimal_num}")
    print(f"Binary: {binary_val}")
    print(f"Hexadecimal: {hex_val}")

if __name__ == "__main__":
    main()