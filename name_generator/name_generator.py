import random


first_name = ["Henry", "Lucy", "Andy", "Mike", "Sarah", "Frank", "Jade", "Shaun", "Louise", "Sandra", "Tom"]
second_name = ["O'Conner", "Smith", "Turner", "Sturrock", "McGhee", "Butler", "Grey", "Thompson"]

def return_random_name():
    print random.choice(first_name) + " " +  random.choice(second_name)

return_random_name()
