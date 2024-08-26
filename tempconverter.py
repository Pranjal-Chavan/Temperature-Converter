while True:
    temp = float(input("Enter temperature :"))
    unit = input("Enter temperature unit (C, F, or K): ").lower()

    if unit == 'c':
        F = float(temp * (9.0/5.0) + 32)
        K = float(temp + 273.15)
        print(f"{temp:.2f} Celsius is {F:.2f} in Fahrenheit and {K:.2f} in Kelvin")

    elif unit == 'f':
        C = float((temp - 32) * 5/9)
        K = float(5/9 *(temp - 32) + 273.15)
        print(f"{temp:.2f} Fahrenheit is {C:.2f} in Celsius and {K:.2f} in Kelvin")

    elif unit == 'k':
        C = float(temp - 273.15)
        F = float((temp - 273.15) * 1.8 + 32)
        print(f"{temp:.2f} Kelvin is {C:.2f} in Celsius and {F:.2f} in Fahrenheit")

    else:
        print("INVALID CHOICE!!")
        print("Please enter correct choice (C, F, or K)")

    continue_loop = input("Do you want to continue? (yes/no): ").lower()
    if continue_loop != 'yes':
        break