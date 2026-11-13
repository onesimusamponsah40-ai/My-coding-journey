import random

while True:
    random_flip = random.choice(["Heads", "Tails"])
    user_input = input("Heads or Tails: ")
    print(random_flip)
    if user_input.capitalize() == random_flip:
        print("You win!")
    else:
        print("Try again")
    Play_again = input("Play again(y/n): ")
    if Play_again.lower() != "y":
        print("Thank you for playing")
        break
    
    

    
        
  
        

    