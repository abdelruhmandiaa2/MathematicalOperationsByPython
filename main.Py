import calc as calculation
import ReadInput as ReadingInput


while True:
    numberOne,numberTwo=ReadingInput.getTwoNumbersWithValidation()
    valid_operations = {'div','sub', 'add', 'mult' }
    switch={
            'add': lambda: calculation.Sum(numberOne, numberTwo),
            'sub': lambda: calculation.Minus(numberOne, numberTwo),
            'mult': lambda: calculation.Multiply(numberOne, numberTwo),
            'div': lambda: calculation.Divide(numberOne, numberTwo)
    }
    while True:
                operation = input(f"Enter operation {valid_operations} ").strip().lower()
                if operation in valid_operations:
                    result  = switch.get(operation)()
                    break
                else:
                    print(f"Invalid operation. Please enter one of the following: {valid_operations}")


    print(result)
    continue_prompt = input("Do you want to perform another operation? (yes/no): ").strip().lower()
    if(continue_prompt=='no'):
       break
      
