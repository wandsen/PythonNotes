birthdays = {
    "alpha" : "12/May/2000",
    "bravo" : "15/April/1900",
    "charlie" : "15/March/1900",
    "delta" : "15/March/1900",
    "echo" : "15/April/1900",
    "foxtrot" : "15/June/1900",
    "giant" : "15/June/1900",
    "hello" : "15/July/1900",
    "imp" : "15/August/1900",
    "jam" : "15/September/1900",
    "kestral" : "15/October/1900"
}
def askBirthday():
    print('Hi')
    user_input  = input("What name?")
    print("Your birthday is + " + birthdays.get(user_input))

if __name__ == '__main__' :
    test()

def getBirthdays():
    return birthdays

