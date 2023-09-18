import random

# TODO: add optional weight for options

options = []
# todo: have a better way of ending the options list in input
print("What are the options you are deciding between? (to stop entering options, enter \"no more options\")")

while True:
    next_option = input()
    if next_option == "no more options":
        break
    options.append(next_option)

selection = random.randint(0, len(options) - 1)
print("The chosen option is: " + str(options[selection]))
