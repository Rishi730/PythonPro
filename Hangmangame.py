#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
lives=10
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')
display=[]
for i in range(len(chosen_word)):
  display.append("_")

print(display)

endofgame=False
while not endofgame:
  guess = input("Guess a letter: ").lower()





  for i in range(len(chosen_word)):
    if chosen_word[i]==guess:
      display[i]=guess

  if guess not in chosen_word:
    print("Not a match ")
    lives=lives-1
    print("Lives remaining : ",lives)
    
  print(display)

  if lives==0:
    endofgame=True
    print("You lose ")
    
  if "_" not in display:
    endofgame=True
    print("You win ")

