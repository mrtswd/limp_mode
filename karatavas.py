import random
from words import word_list # words failam jabut taja pasha mapee kur py fails

# words to uppercase
def get_words():
    word = random.choice(word_list)
    return word.upper()

# definejam attelot tuksumus un meginajumu skaitu
def play(word):
    word_comp = "_" * len(word)
    guessd = False
    guess_lett = []
    guess_words = []
    tries = 6
    print("Uzspēlēsim karātavu jeb vārdu spēli! Bet ņem vērā, ka vārdi ir angļu valodā!")
    print(display_hangman(tries))
    print(word_comp)
    print("\n")
    while not guessd and tries > 0:
        guess = input("Lūdzu mini kādu burtu:  ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guess_lett:
                print("Tu jau šādu burtu minēji: ", guess)
            elif guess not in word:
                print("Diemžēl", guess, " burts nav šajā vārdā")
                tries -= 1
                guess_lett.append(guess)
            else:
                print("Tu uzminēji: ", guess, "burts ir šajā vārdā!")
                guess_lett.append(guess)
                word_as_list = list(word_comp)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_comp = "".join(word_as_list)
                if "_" not in word_comp:
                    guessd = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guess_words:
                print("Tu jau uzminēji šo burtu iepriekš", guess)
            elif guess != word:
                print(guess, "nav šāda burta minamajā vārdā")
                tries -= 1
                guess_words.append(guess)
            else:
                guessd = True
                word_comp = word
        else:
            print("Nederīgs minējums.")
        print(display_hangman(tries))
        print("Minamais vārds: ", word_comp)
        print("Burti, kurus esi jau izmantojis: ", listToString(guess_lett))
        print("\n")
    if guessd:
        print("Apsveicam! Tu uzminēji vārdu. Tu vinnēji!!!!")
    else:
        print("Diemžēl visas iesp­ējas izt­ērētas. Vārds bija: " + word + ". Varbūt veiksies nākamajā reizē!")

def listToString(guess_lett):  
    str1 = " "  
    return (str1.join(guess_lett))

# draw man in terminal
def display_hangman(tries):
    stages = [  # pedejais
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """ 
                ,
                # iepriekspedejais
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # pirmais
                """ 
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_words()
    play(word)
    while input("Spēlēsim vēlreiz? (Y / N) ").upper() == "Y":
        word = get_words()
        play(word)

if __name__ == "__main__":
    main()