import random

# TODO: add optional weight for options

options = []
print("What are the options you are deciding between? (enter each option on a separate line and use a blank line to indicate the end of the list)")

while True:
    next_option = input()
    if len(next_option) == 0:
        break
    options.append(next_option)

selection = random.randint(0, len(options) - 1)
print("The chosen option is: " + str(options[selection]))
