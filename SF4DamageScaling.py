# This program calculates the damage or stun of a combo in the video game
# Ultra Street Fighter 4 based on user inputs for combo length and
# damage or stun values.

import math

# the main function; adds up scaled values for damage/stun
def main():
    val_list = []
    combo_length = checkIfInt()
    for i in range(combo_length):
        val = raw_input("What is the damage/stun of move " + str(i+1) + "? ")
        try:
            val_list += [int(val)]
        except ValueError:
            # takes the user to the start of the program if
            # they do not enter a number
            print "Invalid input. Please enter a number next time."
            print "Restarting:"
            main()
    # prints the damage or stun of the given combo
    print "Your combo does", (scale(val_list)), "damage/stun!"

# checks if the user actually enters a number
def checkIfInt():
    valid = False
    while (not(valid)):
        response = raw_input("How many moves does your combo contain? ")
        try:
            combo_length_int = int(response)
            valid = True
        except ValueError:
            print "Please enter a number."
    return combo_length_int

# performs the scaled summation of moves' damage/stun values
def scale(vals):
    scaled_sum = 0
    for i in range(len(vals)):
        if (i == 0 or i == 1):
            scaled_sum += vals[i]
        elif (i >=2 and i <= 8):
            scaled_sum += math.ceil(vals[i]- (i * 0.1 * vals[i]))
        else:
            scaled_sum += math.ceil(0.1 * val_list[i])
    return int(scaled_sum)

main()

