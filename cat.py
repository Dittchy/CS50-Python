i = int(input("i : "))

def is_even(i):
    if i % 2 == 0:
        return True
    else:
        return False

def main():
    while is_even(i) == True:
        print("meow")

main()
    