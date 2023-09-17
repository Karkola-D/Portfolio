def sieve_of_eratosthenes(n):
  """
  This function implements the Sieve of Eratosthenes algorithm to
  find all prime numbers less than or equal to a given number n.

  Args:
    n: The upper bound for the prime numbers to be found.

  Returns:
    A list of prime numbers less than or equal to n.
  """
  """  
  Die Funktion erstellt eine Liste mit allen Zahlen von 2 bis n:
  
  Bis zur einer endliche zahlen
  """
  primes = []
  is_prime = [True] * (n + 1)

  """  
  Die Funktion markiert alle geraden Zahlen als nicht-prim:
  """
  # Mark all even numbers as non-prime.
  for i in range(2, n + 1, 2):
    is_prime[i] = False



  """  
 Die Funktion beginnt mit der ersten Primzahl, 2, und markiert alle Vielfachen von 2 als nicht-prim:
  """
  # Start with the first prime number, 2.
  p = 2

  while p * p <= n:
    # Mark all multiples of p as non-prime.
    if is_prime[p]:
      for i in range(p * p, n + 1, p):
        is_prime[i] = False

    p += 1
    
  """  
  Die Funktion fügt alle Zahlen in der Liste is_prime, die nicht markiert wurden, in die Liste primes ein:
  """

  # Add all unmarked numbers to the list of primes.
  for i in range(2, n + 1):
    if is_prime[i]:
      primes.append(i)

  return primes


print(sieve_of_eratosthenes((100)))