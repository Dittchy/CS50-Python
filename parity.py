def main():
    x = int(input("What is x ? "))
    if is_even(x):#Only this line uses the function 
        print("Even")
    else:#The function isn't used here
        print("Odd")

def is_even(n):
#    if n % 2 == 0:
#        return True
#    else:
#        return False
    return True if n % 2 == 0 else False


main()