import random

options = ["beaks", "bluer", "skews", "preps", "maths", "eccer", "yards", "grove", "daves", "rugby", "knoll", "shell", "house", "field", "songs", "essay", "chess", "choir", "cadet", "corps", "study", "drill", "forty", "steps", "byron", "lyons"]
secret = random.choice(options)
secret_list = []
attempt_list = []
guesses = 0
user_guess = [" ", " ", " ", " ", " "]
grid = [[],[],[],[],[]]


def splitting(arg, arg_list):
  for i in range(len(arg)):
    arg_list.append(arg[i])

def compare(x, y):
  for i in range(5):
    if y[i] == x[i]:
      user_guess[i] = x[i]

def highlight(j):
  for i in range(len(j)):
    if j[i] == secret_list[i]:
      grid[guesses].append((f"*{j[i].upper()}*"))
      continue
    elif j[i] in secret_list:
      grid[guesses].append(j[i].upper())
      continue
    else:
      grid[guesses].append(j[i])

def decor(m):
  print(f'------{"-"*len(m[0])}{"-"*len(m[1])}{"-"*len(m[2])}{"-"*len(m[3])}{"-"*len(m[4])}')
  print(f'¦{m[0]}¦{m[1]}¦{m[2]}¦{m[3]}¦{m[4]}¦')
  print(f'------{"-"*len(m[0])}{"-"*len(m[1])}{"-"*len(m[2])}{"-"*len(m[3])}{"-"*len(m[4])}')
      


print('''
Welcome to Harrow Wordle! 
Try to guess the Harrow word in 5 tries. 
--------------
If letter == upper case, it is somewhere in the hidden word. 
--------------
If letter == upper case and surrounded by "**": it is in the hidden word and in the correct position in the hidden word.
--------------
If letter != upper case: letter not in word
--------------

''')

splitting(secret, secret_list)

while guesses < 5:
  attempt_list = []
  attempt = input("Enter a five letter guess: ")
  attempt = attempt.lower()
  
  
  if len(attempt) != 5:
    print("len(word) has to == 5 char")
    continue

  splitting(attempt, attempt_list)
  compare(secret_list, attempt_list)
  highlight(attempt_list)


  decor(grid[guesses])
  guesses += 1

  
  if attempt == secret:
    print(f'The word was {secret}!')
    break

  if guesses == 5:
    print('You ran out of guesses!')
    print(f'The word was {secret}!')