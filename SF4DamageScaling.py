import math

def main():
    val_list = []
    combo_length = checkIfInt()
    for i in range(combo_length):
        val = raw_input("What is the damage/stun of move " + str(i+1) + "? ")
        try:
            val_list += [int(val)]
        except ValueError:
            print "Invalid input. Please enter a number next time."
            print "Restarting:"
            main()
    comboDamage = 0
    for i in range(len(val_list)):
        if (i == 0 or i == 1):
            comboDamage += val_list[i]
        elif (i >=2 and i <= 8):
            comboDamage += math.ceil(val_list[i]- (i * 0.1 * val_list[i]))
        else:
            comboDamage += math.ceil(0.1 * val_list[i])
    print "Your combo does", int(comboDamage), "damage/stun!"

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

main()
