# prints message to terminal
print("Rules that govern the state of water")

# set up var to hold temp we input
current_temp = False

while current_temp is False:
    current_temp = input("Enter a temperature\n")
    print("you input:", current_temp)

    # if the current temp is at freezing or below, water is solid
    if (int(current_temp) < 0 or (int(current_temp) == 0)):
        print("water is solid! Cuz its below freezing")
        current_temp = False
    # else check another condition, if its not freezing , is below boiling
    elif (int(current_temp) < 100):
        print("water is a liquid, because it is above freezing and below boiling")
        current_temp = False
    elif (int(current_temp) > 100 or int(current_temp) == 100):
        print("water is a gas, cuz its like, really hot")
        current_temp = False
