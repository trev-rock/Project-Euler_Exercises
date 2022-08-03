total = 0  # this is our total of how many letters have been used


def convert_1(i):  # method for generating 1-19
    if i == 1:
        return "one"
    if i == 2:
        return "two"
    if i == 3:
        return "three"
    if i == 4:
        return "four"
    if i == 5:
        return "five"
    if i == 6:
        return "six"
    if i == 7:
        return "seven"
    if i == 8:
        return "eight"
    if i == 9:
        return "nine"
    if i == 10:
        return "ten"
    if i == 11:
        return "eleven"
    if i == 12:
        return "twelve"
    if i == 13:
        return "thirteen"
    if i == 14:
        return "fourteen"
    if i == 15:
        return "fifteen"
    if i == 16:
        return "sixteen"
    if i == 17:
        return "seventeen"
    if i == 18:
        return "eighteen"
    if i == 19:
        return "nineteen"


def convert_2(i):  # this converts a number to a string and evaluates first if it is a base 10 we just say that number by itself otherwise we say (for example) twenty one
    # these are for when we are in the hundreds
    # even though in convert_3 we are taking int(i[1] + i[2]), when i[1] == 0 the resulting integer is not going to have a zero in front of it so that's why we can use convert_1
    if i < 20:
        return convert_1(i)
    if i >= 20 and i <= 29:
        i = str(i)
        if i[-1] == "0":
            return "twenty"
        else:
            # the second part is an f string an d in the brackets we have it using the convert_1 method with converting the ones digit back to an integer (it is the ones because of the [1])
            return f"twenty {convert_1(int(i[-1]))}"
    if i >= 30 and i <= 39:
        i = str(i)
        if i[-1] == "0":
            return "thirty"
        else:
            return f"thirty {convert_1(int(i[-1]))}"
    if i >= 40 and i <= 49:
        i = str(i)
        if i[-1] == "0":
            return "forty"
        else:
            return f"forty {convert_1(int(i[-1]))}"
    if i >= 50 and i <= 59:
        i = str(i)
        if i[-1] == "0":
            return "fifty"
        else:
            return f"fifty {convert_1(int(i[-1]))}"
    if i >= 60 and i <= 69:
        i = str(i)
        if i[-1] == "0":
            return "sixty"
        else:
            return f"sixty {convert_1(int(i[-1]))}"
    if i >= 70 and i <= 79:
        i = str(i)
        if i[-1] == "0":
            return "seventy"
        else:
            return f"seventy {convert_1(int(i[-1]))}"
    if i >= 80 and i <= 89:
        i = str(i)
        if i[-1] == "0":
            return "eighty"
        else:
            return f"eighty {convert_1(int(i[-1]))}"
    if i >= 90 and i <= 99:
        i = str(i)
        if i[-1] == "0":
            return "ninety"
        else:
            return f"ninety {convert_1(int(i[-1]))}"


def convert_3(i): # if the number is an even multiple of 100 we say "whatever number it is hundred", otherwise we say "whatever number it is hundred and convert_2"
    if i >= 100 and i <= 199:
        i = str(i)
        if i[1] == "0" and i[2] == "0":
            return "one hundred"
        else:
            return f"one hundred and {convert_2(int(i[1]+i[2]))}"
    if i >= 200 and i <= 299:
        i = str(i)
        if i[1] == "0" and i[2] == "0":
            return "two hundred"
        else:
            return f"two hundred and {convert_2(int(i[1]+i[2]))}"
    if i >= 300 and i <= 399:
        i = str(i)
        if i[1] == "0" and i[2] == "0":
            return "three hundred"
        else:
            return f"three hundred and {convert_2(int(i[1]+i[2]))}"
    if i >= 400 and i <= 499:
        i = str(i)
        if i[1] == "0" and i[2] == "0":
            return "four hundred"
        else:
            return f"four hundred and {convert_2(int(i[1]+i[2]))}"
    if i >= 500 and i <= 599:
        i = str(i)
        if i[1] == "0" and i[2] == "0":
            return "five hundred"
        else:
            return f"five hundred and {convert_2(int(i[1]+i[2]))}"
    if i >= 600 and i <= 699:
        i = str(i)
        if i[1] == "0" and i[2] == "0":
            return "six hundred"
        else:
            return f"six hundred and {convert_2(int(i[1]+i[2]))}"
    if i >= 700 and i <= 799:
        i = str(i)
        if i[1] == "0" and i[2] == "0":
            return "seven hundred"
        else:
            return f"seven hundred and {convert_2(int(i[1]+i[2]))}"
    if i >= 800 and i <= 899:
        i = str(i)
        if i[1] == "0" and i[2] == "0":
            return "eight hundred"
        else:
            return f"eight hundred and {convert_2(int(i[1]+i[2]))}"
    if i >= 900 and i <= 999:
        i = str(i)
        if i[1] == "0" and i[2] == "0":
            return "nine hundred"
        else:
            return f"nine hundred and {convert_2(int(i[1]+i[2]))}"


for i in range(1, 1001):
    if i < 20:
        word = convert_1(i)
        print(word)
        total += len(word)
    elif i >= 20 and i < 100:
        word = convert_2(i)
        print(word)
        # this replaces the whitespace of the word from "twenty one" to "twentyone", which is what we need for the letter count otherwise the white space will count towards it
        total += len(word.replace(" ", ""))
    elif i >= 100 and i <= 999:
        word = convert_3(i)
        print(word)
        total += len(word.replace(" ", ""))
    else:
        word = "one thousand"
        print(word)
        total += len(word.replace(" ", ""))


print(total)
