def fibonacci(n):
  """
  Berechnet die Fibonacci-Folge bis zu n.

  Args:
    n: Die Anzahl der Fibonacci-Zahlen.

  Returns:
    Eine Liste mit den Fibonacci-Zahlen.
  """
  if n == 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 1]
  else:
    result = fibonacci(n - 1)
    result.append(result[-1] + result[-2])
    return result

print(fibonacci(10))

"""
Die Fibonacci-Zahlen  

Die Fibonacci-Zahlen sind folgendemaßen rekrusiv definert 
F1 = 1 ~ n == 1
F2 = 2 ~ n == 2
Fn = Fn -1 + Fn -2  n>2 ~ (result[-1] + result[-2])


"""