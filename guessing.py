import random

number=random.randint(1,100)
tries=0
prev_guess=set()

print("="*80)
print("Welcome")
print("="*80)

while(True):
    user_inp=input("Guess A Number (1-100):")
    
    if not user_inp.isdigit():
        print("Enter a Valid Input..!")
        continue
        
    guess=int(user_inp)
        
    if guess in prev_guess:
        print("You have already guessed this.! try diff number.\n")
        continue
    
    prev_guess.add(guess)
    tries+=1
    
    if guess==number:
        print(f"You Found The number..! ,in {tries} attempts.\n")  
        break
    
    elif guess>number:
        print("Number is smaller.\n")
    else:
        print("Number is Larger.\n")