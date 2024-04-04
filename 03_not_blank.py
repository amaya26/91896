# function goes here

# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs an error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# main routine goes here
tickets_sold = 0

while True:
    name = not_blank("Enter your name (or 'xxx' to quit) ")
    if name == "xxx":
        break

    age = int(input("Age: "))

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie")
        continue
    else:
        print("?? That looks like a typo, please try again.")
        continue

    tickets_sold += 1

print("We are done")
