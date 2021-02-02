#variable controls loop and holds operation choice
val_operation = -1

#function that calculates inputs base of operation choice
def calc(num1, num2, op):
  if(op == 1):
    return num1+num2
  elif(op == 2):
    return num1-num2
  elif(op == 3): 
    return num1*num2
  elif(op == 4): 
    return num1/num2

#while loop that controls the game. Game on until choice 0 is chosen
while(val_operation !=0):
  print("---Python Basics Calculator Game---\n")
  
  #variables that hold number input. Variables also casted to float type
  val_1 = float(input("1st Input: "))
  val_2 = float(input("2nd Input: "))

  print("\nPick an Operation:\n1) Add\n2) Subtract\n3) Multiply\n4) Divide\n0) Exit")
 
  #var changes operation choice value
  val_operation = int(input("Choice: "))

  #calc function is ran to compute operation
  final_value = calc(val_1, val_2, val_operation)
  print("\nAnswer: " + str(final_value)+"\n")
