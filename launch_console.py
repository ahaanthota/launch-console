name = input("Hello! My name's Ahaan Thota. What's your name? ")
print("Welcome to my Launch Console, " + name + "! It's nice to meet you.")

running = True
while running:
    print("1) About me")
    print("2) My goals")
    print("3) Exit")
    choice = input("Pick 1-3: ")
    if choice == "1":
        print("I'm currently a junior at Dulles High School. I like building AI models and doing research. For fun, I play the violin and spend time with my friends.")
    elif choice == "2":
        print("I want to build an effective startup that is used by people around the world.")
    elif choice == "3":
        print("Goodbye! It was nice talking to you " + name + "!")
        running = False
    else:
        print("Please pick 1, 2, or 3.")