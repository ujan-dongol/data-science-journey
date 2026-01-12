
secret_number = 7 
guess = 0 

while guess != secret_number:
    guess = int(input("Guess the number : "))
    
    
    if guess == secret_number:
        print(f"Correct! You have guessed it the correct number.Yes the secret number is {guess}")
        
    else:
        print(f"Oopps!You have guessed it the Wrong number.{guess} is not that secret number.Try Again.")