print("🎬 WELCOME TO CINEMA WORLD 🎬")
print("Book your tickets easily!\n")

# Movie menu with prices
movies = {
    1: ("Avengers: Endgame", 300),
    2: ("Spider-Man: No Way Home", 250),
    3: ("The Batman", 280),
    4: ("Frozen 2", 200)
}

# Available seats per movie
seats = {
    1: 50,
    2: 40,
    3: 30,
    4: 60
}

total_amount = 0

while True:
    print("\n------ MOVIES ------")
    for key in movies:
        print(f"{key}. {movies[key][0]} - Rs {movies[key][1]} (Seats available: {seats[key]})")
    
    choice = int(input("\nEnter movie number to book (0 to finish): "))
    
    if choice == 0:
        break
    elif choice in movies:
        if seats[choice] == 0:
            print("❌ Sorry, no seats available for this movie.")
            continue
        
        qty = int(input("Enter number of tickets: "))
        
        if qty > seats[choice]:
            print(f"❌ Only {seats[choice]} seats are available. Try again.")
            continue
        
        seats[choice] -= qty
        price = movies[choice][1] * qty
        total_amount += price
        
        print(f"✅ {qty} tickets for '{movies[choice][0]}' booked! Subtotal: Rs {price}")
    else:
        print("❌ Invalid choice. Try again!")

# Applying discount
if total_amount >= 1000:
    discount = total_amount * 0.1
    total_amount -= discount
    print(f"\n🎉 10% Discount Applied: Rs {discount}")

print("\n🧾 FINAL BILL: Rs", total_amount)
print("Thank you for booking with Cinema World! Enjoy your movie! 🍿")