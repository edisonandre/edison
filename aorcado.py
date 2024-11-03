import random

def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
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

def play_hangman():
    word_list = ['python', 'programacion', 'juego', 'computadora', 'codigo', 'casa', 'colegio', 'celular', 'colombia', 'variable', 'bucle', 'funcion', 'modulo', 'objeto','clase', 'lista', 'diccionario', 'tupla', 'condicional', 'iteracion', 'excepcion', 'argumento', 'parametro', 'decorador', 'herencia', 'importacion', 'cadena', 'flotante', 'booleano']
    word = random.choice(word_list)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("¡Juguemos al Ahorcado!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Adivina una letra o la palabra: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Ya adivinaste la letra", guess)
            elif guess not in word:
                print(guess, "no está en la palabra.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("¡Bien hecho,", guess, "está en la palabra!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Ya adivinaste la palabra", guess)
            elif guess != word:
                print(guess, "no es la palabra.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("No es una suposición válida.")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("¡Felicidades! Adivinaste la palabra:", word)
    else:
        print("Lo siento, te quedaste sin intentos. La palabra era:", word)

play_hangman()
