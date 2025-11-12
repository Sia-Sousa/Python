import random

answer = 'Y'
symbols = ['🍒', '🍇', '🍉', '7️⃣']

while answer != 'N' :
  answer = input("Last play 🎮 (N to stop)? ").upper()

  if answer != 'N':
    results = random.choices(symbols, k=3) 
    print(f"{results[0]} | {results[1]} | {results[2]}")

    if results == ['7️⃣','7️⃣','7️⃣']:
      print ("Jackpot! 💰\n")
    else:
      print ("Thanks for playing!\n")

print ("Fim")
