#match keyword
name = input("What is your name? ")

match name :
    case "Harry" | "Hermoione" | "Ron":#And jaisa sa hai ye kuch
        print("Gryffindor")
    case "Draco":
        print("Slytherine")
    case _:
        print("Who? ")