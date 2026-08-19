# TO-DO Initialize the authorized variable
users = []
authorized = False

fileHandle = open("authorized_users.txt", "r")
data = fileHandle.readlines()
fileHandle.close()

for d in data:
    tmp = d.strip().split(",")

    user = {}
    user["username"] = tmp[0]
    user["pass"] =tmp[1]
    user["level"] = int(tmp[2])

    users.append(user)

# TO-DO Prompt user for username/password
username = input("Enter your username: ")
password = input("Enter your password: ")
# TO-DO Compare input username and password with authorized users file
for user in users:
    if user["username"] == username and user["pass"] == password:
        authorized = True
        authorized_level = user["level"]
        break
# THEN, if authorized is True, run the code from tilling_the_soil.py by copying the necessary code in the BOTTOM 
if authorized:
    print("Access granted. Welcome!")
    # Here you would include the code from tilling_the_soil.py
    import math

    print('Welcome to the Fertilizer Calculator! I will ask you for the length and width of four rectangular sections. \nPlease enter your measurements in feet (numbers only, please). If you do not have a particular section, simply enter zero (0) for those dimensions! \nPress ENTER to start!')
    # The beginning print statement has been written, WRITE YOUR CODE BELOW:
    print()
    # TO-DO Collect dimensions
    print("please enter the dimensions for Lawn 1.")
    print()
    lawn1_length = float(input("Enter the length of Lawn 1: "))
    lawn1_width = float(input("Enter the width of Lawn 1: "))
    print()
    print("please enter the dimensions for Lawn 2.")
    print()
    lawn2_length = float(input("Enter the length of Lawn 2: "))
    lawn2_width = float(input("Enter the width of Lawn 2: "))
    print()
    print("please enter the dimensions for Lawn 3.")
    print()
    lawn3_length = float(input("Enter the length of Lawn 3: "))
    lawn3_width = float(input("Enter the width of Lawn 3: "))
    print()
    print("please enter the dimensions for Lawn 4.")
    print()
    lawn4_length = float(input("Enter the length of Lawn 4: "))
    lawn4_width = float(input("Enter the width of Lawn 4: "))
    print()
    # TO-DO Calculate areas
    lawn1_area = lawn1_length * lawn1_width
    lawn2_area = lawn2_length * lawn2_width
    lawn3_area = lawn3_length * lawn3_width
    lawn4_area = lawn4_length * lawn4_width

    # TO-DO Total area
    total_area = lawn1_area + lawn2_area + lawn3_area + lawn4_area

    # TO-DO Calculate the number of bags of fertilizer
    actual_bags = total_area / 2000
    number_of_bags = math.ceil(actual_bags)

    # TO-DO Calculate the cost of fertilizer
    fertilizer_cost = number_of_bags * 27

    # TO-DO Calculate labor hours and cost
    labor_hours = math.ceil(total_area / 2500)
    labor_cost = labor_hours * 20

    # TO-DO Total cost
    total_cost = fertilizer_cost + labor_cost

    # TO-DO Calculate the amount of nitrogen and potassium
    nitrogen = actual_bags * 1
    potassium = actual_bags * .125
    # TO-DO Output the results
    print()
    print("==========CALCULATION SUMMARY==========")
    print(f"The total area: {total_area} square feet")
    print(f"Number of Bags: {number_of_bags}")
    print(f"Cost of fertilizer: ${fertilizer_cost:.2f}")
    print(f"Labour Hours: {labor_hours}")
    print(f"Cost of labor: ${labor_cost:.2f}")
    print(f"Total cost: ${total_cost:.3f}")
    print(f"Nitrogen Applied: {nitrogen:.3f} pounds")
    print(f"Potassium Applied: {potassium:.3f} pounds")

else:
    print("Credentials are invalid. Re-enter your username and password..")
    quit()