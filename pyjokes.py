import pyjokes

def tell_joke():
    joke = pyjokes.get_joke()
    print(f"Here's a joke for you: {joke}")

if __name__ == "__main__":
    while True:
        user_input = input("Do you want to hear a joke? (yes/no): ")
        if user_input.lower() == "yes":
            tell_joke()
        else:
            break
