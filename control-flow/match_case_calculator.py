x = int(input ("Enter the first number: "))
y = int(input ("Enter the second number: "))
operation = input ("Choose the operation (+, -, *, /): ")

match operation:

    case '+':
        print(f"the result is {x+y}")

    case '-':
         print(f"the result is {x+y}")

    case "/":
         if (y == 0):
             print ("Cannot divide by zero.")

         else:
             print(f"the result is {x+y}")

    case "*":
          print(f"the result is {x+y}")
