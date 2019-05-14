import pdb

def print_sammy():
    sammy_list = []
    sammy = "sammy"

    #trigger debugger at this line
    pdb.set_trace()

    for letter in sammy:
        sammy_list.append(letter)
        print(sammy_list)

if __name__ == "__main__":
    print_sammy()