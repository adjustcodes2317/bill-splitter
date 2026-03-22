def equal_split():

    total = float(input("enter total bill : "))
    n = int(input("how many people : "))

    names = []
    for i in range(n):
        name = input("enter name : ")
        names.append(name)

    each = total / n

    print("\nresult --")
    for name in names:
        print(name, "has to pay", each)

    # who owes whom
    # in equal split, everyone owes the first person who paid
    print("\nwho owes whom --")
    payer = names[0]
    for name in names[1:]:
        print(name, "owes", payer, "-->", each)


def custom_split():

    n = int(input("how many people : "))

    names = []
    amounts = []

    for i in range(n):
        name = input("name : ")
        amt = float(input("how much did they order : "))
        names.append(name)
        amounts.append(amt)

    total = 0
    for amt in amounts:
        total = total + amt

    # figure out the average share
    avg = total / n

    print("\nresult --")
    print("total bill is", total)
    for i in range(n):
        print(names[i], "pays", amounts[i])

    # who owes whom
    # if someone paid less than average they owe money
    # if someone paid more than average they get money back
    print("\nwho owes whom --")
    for i in range(n):
        diff = amounts[i] - avg
        if diff < 0:
            print(names[i], "owes", round(abs(diff), 2), "to the group")
        elif diff > 0:
            print(names[i], "should get back", round(diff, 2), "from the group")
        else:
            print(names[i], "is settled")


# main program starts here

print("welcome to bill splitter")
print("1. split equally")
print("2. split by what each person ordered")
print("3. exit")

while True:
    ch = input("\nenter choice : ")

    if ch == "1":
        equal_split()
    elif ch == "2":
        custom_split()
    elif ch == "3":
        print("bye!")
        break
    else:
        print("wrong input try again")
