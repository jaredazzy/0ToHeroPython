#This part of the code we are creating a function that will help us determine the plural form based off the noun.
#So we are using the if elif statements to let the program know what to do based using the rules provided in the prompt table
def plural(noun):
    if noun.endswith(("ch", "sh", "s", "x", "z")):
        return noun + "es"
    elif noun.endswith("y") and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"
    elif noun.endswith("f"):
        return noun[:-1] + "ves"
    elif noun.endswith("fe"):
        return noun[:-2] + "ves"
    else:
        return noun + "s"

#Now that we've created a function to define the rule, this part of the code is so we can ask the user for it's input
#And then apply the function from above into the print statement
noun = input("Please enter a word: ")
plural_noun = plural(noun)
print(f"The plural form of {noun} is {plural_noun}.")

