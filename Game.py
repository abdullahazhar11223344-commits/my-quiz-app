import random

print("--- PYTHON NUMBER GUESSING GAME BY ABDULLAH ---")

best_score = 9999  # Shuru mein best score ko bohot bara rakhte hain

while True:
    print("\nComputer ne 1 se 100 ke darmiyaan aik number soch liya hai.")
    print("Dekhte hain aap kitni koshishon mein sahi number guess karte hain!\n")

    sahi_number = random.randint(1, 100)
    koshishein = 0

    while True:
        user_guess = int(input("Apna guess kiya hua number likhein (1-100): "))
        koshishein = koshishein + 1

        if user_guess < sahi_number:
            print("Oho! Thoda BARA (higher) number do bhai.\n")
        elif user_guess > sahi_number:
            print("Oho! Thoda CHOTA (lower) number do bhai.\n")
        else:
            print(f"🎉 Mubarak ho! Aap ne bilkul sahi number ({sahi_number}) guess kar liya hai!")
            print(f"Aap ne is baar kul {koshishein} koshishein (attempts) ki hain.\n")
            
            # Check karenge ke kya yeh sab se behtareen record hai
            if koshishein < best_score:
                best_score = koshishein
                print("🌟 Wah bhai! Aap ne naya record bana liya hai (Best Score)!\n")
            
            print(f"Aap ka abhi tak ka sab se behtareen score (Best Attempt): {best_score}\n")
            break

    # Game khatam hone ke baad user se poochenge
    dobara = input("Kya aap mazeed game khelna chahte hain? (han/nahi): ")
    if dobara.lower() != 'han':
        break

# Jab user 'nahi' kahega tab yeh aakhri line chalegi
input("\nChlo ab bhari chaya jaoo! Bahar nikalne ke liye Enter dabayein...")