# Import 'math' and 'time' libraries
import math, time


# Display welcome message
print("\nWelcome to the Tip Calculator.")


# Get total bill, tip percentage and number of people, and store it in 'total_bill' (Float), 'tip_percentage' (String) and 'number_of_people' (Float) respectively
while True:
    try:
        total_bill = float(input("\nWhat was the total bill?\n$"))
        if total_bill > 0:
            tip_percentage = input("\nWhat percentage of tip would you like to give? (5%, 10% or 15%)\n")
            if tip_percentage == "5%" or tip_percentage == "5":
                tip_percentage = 0.05
                number_of_people = math.ceil(float(input("\nHow many people will the bill be split between?\n")))
                if number_of_people >= 1:
                    break
                else:
                    print("\nInvalid input. Only numbers above or equal to 1 are accepted.")
            elif tip_percentage == "10%" or tip_percentage == "10":
                tip_percentage = 0.10
                number_of_people = math.ceil(float(input("\nHow many people will the bill be split between?\n")))
                if number_of_people >= 1:
                    break
                else:
                    print("\nInvalid input. Only numbers above or equal to 1 are accepted.")
            elif tip_percentage == "15%" or tip_percentage == "15":
                tip_percentage = 0.15
                number_of_people = math.ceil(float(input("\nHow many people will the bill be split between?\n")))
                if number_of_people >= 1:
                    break
                else:
                    print("\nInvalid input. Only numbers above or equal to 1 are accepted.")
            else:
                print("\nInvalid input. Only listed options are accepted.")
        else:
            print("\nInvalid input. Only numbers above 0 are accepted.")
    except ValueError:
        print("\nInvalid input. Only numbers are accepted.")


# Calculate new total bill after adding tip and store it in 'total_bill' (Float)
total_bill += total_bill * tip_percentage


# Calculate amount payable per person, round it to 2 decimal places, and store it in 'payable_per_person' (Float)
payable_per_person = round(total_bill / number_of_people, 2)


# Diplay amount to be paid per person
print(f"\nEach person should pay:\n${payable_per_person:.2f}")


# Display exit message
print("\nProgram exiting...")


# Exit program
for delay in range(5):
    time.sleep(1)
