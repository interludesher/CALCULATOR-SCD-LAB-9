def convert_temp():
    temp = float(input("Enter temperature: "))
    unit = input("Convert to (C/F): ").upper()

    if unit == "C":
        result = (temp - 32) * 5/9
        print("Temperature in Celsius =", result)

    elif unit == "F":
        result = (temp * 9/5) + 32
        print("Temperature in Fahrenheit =", result)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    convert_temp()