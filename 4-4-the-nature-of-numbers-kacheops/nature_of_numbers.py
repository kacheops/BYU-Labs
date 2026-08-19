# TO-DO import math
import math
print("Welcome to the Nature of Numbers Program!")
run_program = True
while run_program:
    number = int(input("\nEnter your favourite number: "))
    print("\nResults:")
# TO-DO Determine if number is even or odd
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
# TO-DO Determine if number has perfect square root
    square_root = math.sqrt(number)
    if square_root == int(square_root):
        print(f"{number} has a perfect square root({int(square_root)}).")
    else:
        print(f"{number} does not have a perfect square root.")
# TO-DO Determine all factors of number
    print(f"The factors of {number} are:")
    if number == 0:
        print("All numbers are factors of 0.")
    else:
        for possible_factor in range(1, abs(number) + 1):
            if number % possible_factor == 0:
                print(possible_factor, end=" ")

# CONTINUE OR EXIT PROGRAM
    print()
    choice = input("\nWould you like to check another number? (yes/no): ")
    if choice.lower() == "no" or choice.lower() == "n":
        run_program = False

print()
print("\nThank you for Playing!")


