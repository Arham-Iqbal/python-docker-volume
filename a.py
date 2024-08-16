import os

FILE_NAME = "/python-volume/names.txt"
names = []

def load_names():
    """Load names from the file if it exists."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                names.append(line.strip())

def save_names():
    """Save names to the file."""
    with open(FILE_NAME, "w") as file:
        for name in names:
            file.write(f"{name}\n")

def add_name():
    """Add a new name and save it."""
    name = input("Enter a name to add: ")
    names.append(name)
    save_names()  # Save names to the file
    print(f"{name} has been added.\n")

def display_names():
    """Display the list of names."""
    if names:
        print("\nList of names:")
        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")
    else:
        print("\nNo names have been added yet.")
    print()

def main():
    """Main menu loop."""
    load_names()  # Load names at the start

    while True:
        print("Options:")
        print("1) Add name")
        print("2) Display names")
        print("3) Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_name()
        elif choice == '2':
            display_names()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
