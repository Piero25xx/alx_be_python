x = input ("Enter the first number: ")
y = input ("Enter the second number: ")
operation = input ("Choose the operation (+, -, *, /): ")

match operation:
    case + : 
        print ("The result is ", x+y)

     case - :
         print ("The result is ", x-y)
