def getTwoNumbersWithValidation():
      while True:
        try:
            number_one = float(input("Enter the first number: "))
            break  
        except :
            print("Invalid input. Please enter a valid number.")

      while True:
        try:
            number_two = float(input("Enter the second number: "))
            break  
        except :
            print("Invalid input. Please enter a valid number.")

      return number_one, number_two



   
    