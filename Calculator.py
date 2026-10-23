print("--- PYTHON CALCULATOR BY ABDULLAH ---")

# Loop shuru karte hain taake bar bar chal sake
while True:
    # Operations dikhayein
    print("\nOperation chuniye:")
    print("1. Jama (+)")
    print("2. Tafreeq (-)")
    print("3. Zarb (*)")
    print("4. Taqseem (/)")
    print("5. Square nikalna (x²)")

    choice = input("Apni pasand ka number likhein (1/2/3/4/5): ")

    # Agar choice 5 hai toh sirf aik number chahiye
    if choice == '5':
        num = float(input("\nAap kis number ka square nikalna chahte hain: "))
        result = num * num
        print(f"Jawab: {num} ka square = {result}")

    # Agar choice 1 se 4 ke darmiyaan hai toh do numbers chahiye
    elif choice in ['1', '2', '3', '4']:
        num1 = float(input("\nPehla number darj karein: "))
        num2 = float(input("Doosra number darj karein: "))

        if choice == '1':
            result = num1 + num2
            print(f"Jawab: {num1} + {num2} = {result}")

        elif choice == '2':
            result = num1 - num2
            print(f"Jawab: {num1} - {num2} = {result}")

        elif choice == '3':
            result = num1 * num2
            print(f"Jawab: {num1} * {num2} = {result}")

        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"Jawab: {num1} / {num2} = {result}")
            else:
                print("Ghalati: Kisi bhi number ko 0 se taqseem nahi kiya ja sakta!")
    else:
        print("Aap ne ghalat option chuna hai! Kripya 1 se 5 ke darmiyaan number dein.")

    # User se poochenge ke kya dobara chalana hai ya nahi
    duwara = input("\nKya aap mazeed calculation karna chahte hain? (han/nahi): ")
    if duwara.lower() != 'han':
        break

# Jab loop khatam hoga toh yeh aakhri line chalegi
input("\nChlo ab bhari chaya jaoo! Bahar nikalne ke liye Enter dabayein...")