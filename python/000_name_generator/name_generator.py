from random import choice


first_name = ["Henry", "Lucy", "Andy", "Mike", "Sarah", "Frank", "Jade", "Shaun", "Louise", "Sandra", "Tom"]
second_name = ["O'Conner", "Smith", "Turner", "Sturrock", "McGhee", "Butler", "Grey", "Thompson"]

def return_random_name():
    print choice(first_name) + " " +  choice(second_name)
exit = False

while exit == False:
    res = raw_input("Press 'Y' for a Random name, and 'X' to exit:   ").upper()
    if res == 'Y': return_random_name()
    if res == 'X': exit = True
