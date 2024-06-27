x = int(input ("Enter the first number: "))
y = int(input ("Enter the second number: "))
operation = input ("Choose the operation (+, -, *, /): ")

match operation:

    case '+':
        print ("The result is ", x+y,".")

    case '-':
         print ("The result is ", x-y,".")

    case "/":
         if (y == 0):
             print ("Cannot divide by zero.")

         else:
             print ("The result is ", x/y,".")

    case "*":
          print ("The result is ", x*y,".")
