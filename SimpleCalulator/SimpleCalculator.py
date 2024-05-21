print(f'______Simple Calculator______')
from typing import Union
 

firstNumber : Union[int, float] = int(input(f"\n Enter first number: "))
secondNumber : Union[int, float] = int(input(f"\n Enter second number:"))

choice = int(input('''
Type following number to choose operation 
1. Add
2. Subtract
3. Multiply
4. Divide
5. Squre
6. Cube
7. Exit
'''))

if choice == 1:
    print(firstNumber + secondNumber)
elif choice == 2:
    print(firstNumber - secondNumber)
elif choice == 3:
    print(firstNumber * secondNumber)
elif choice == 4:
    print(firstNumber / secondNumber)
elif choice == 5:
    print(firstNumber * firstNumber)
elif choice == 6:
    print(firstNumber * firstNumber * firstNumber)
elif choice == 7:
    exit()
else:
    print('Invalid choice')