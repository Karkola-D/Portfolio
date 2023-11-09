import random

def martingale(initial_bet, rounds):
  """
  Simuliert das Martingale-Spiel für die angegebenen Runden.
  Simulates the Martingale-game for the given rounds 

  Args:
    initial_bet: Die Anfangsbeting
    rounds: Die Anzahl der Runden
    
    initial_bet: The initial bet rounds: The number of rounds

  Returns:
    Eine Liste der Gewinne oder Verluste
    A list of wins and losses 
  """
  startWertBank = 1000
  bankkonto = startWertBank
  
  wins = []
  losses = []
  bet = initial_bet
  for _ in range(rounds):
    win = random.choice([True, False])
    if win:
      wins.append(bet)
      bet = initial_bet
    else:
      bet *= 2
      losses.append(bet)
  return wins, losses

if __name__ == "__main__":
  wins, losses = martingale(2, 10)
  print(f"Gewinne: {wins}")
  print(f"Verluste: {losses}")
  print(f"Anzahl der Wins: {len(wins)}")
  print(f"Anzahl der Verluste: {len(losses)}")
  
  
  