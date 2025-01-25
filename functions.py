def abuser(name, level):
    match level:
        case "easy":
            string = f"{name} teri maa ki tan tana tan"
        case "medium":
            string = f"{name} teri bhen ki tan tana tan"
        case "hard":
            string = f"{name} tu bkl hai"
        case "god mod":
            string = f"{name} andi bandii sandii agay kud jhod le"
        case _:
            print("Gali deni buri baat hai")

    print(string);


abuser("kaspar","hard");
