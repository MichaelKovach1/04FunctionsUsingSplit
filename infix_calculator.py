def infix_calculator(expression):
  n1, s, n2 = expression.split(" ")
  n1 = int(n1)
  n2 = int(n2)
  if s == "+":
   return n1 + n2
  elif s == "-":
    return n1 - n2
  elif s == "*":
    return n1 * n2
  elif s == "/":
    return n1 / n2

print("Enter an Equation")
eq = input()
print(eq, "=", infix_calculator(eq))