def save_transaction(Price, credit_card, description):
  file = open("transactions.txt","a")
  file.write("%16s%07d%16s\n" % (credit_card, price * 100, description))
  file.close()
  
items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.20, 1.80, 1.20]
running = true

while running:
  option = 1
  for choice in items:
    print(str(option) + ". " + cloice)
    option = option + 1
    print(str(option) + ". Quit")
    choice = int(input("Choose an option: "))
    if choice == option:
      running = false
    else:
      credit_card = input("credit card number: ")
      save_transaction(prices[choice -1], credit_card, items[choice - 1])
      
      
      
      
