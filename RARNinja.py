import rarfile; import time
from colorama import init
from termcolor import colored

correctPath = False
rarfile.UNRAR_TOOL = "UnRAR.exe"

BANNER1 = colored('''
                         ██▀███   ▄▄▄       ██▀███   ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
                        ▓██ ▒ ██▒▒████▄    ▓██ ▒ ██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
                        ▓██ ░▄█ ▒▒██  ▀█▄  ▓██ ░▄█ ▒▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
                        ▒██▀▀█▄  ░██▄▄▄▄██ ▒██▀▀█▄  ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
                        ░██▓ ▒██▒ ▓█   ▓██▒░██▓ ▒██▒▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
                        ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
                          ░▒ ░ ▒░  ▒   ▒▒ ░  ░▒ ░ ▒░░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
                          ░░   ░   ░   ▒     ░░   ░    ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
                           ░           ░  ░   ░              ░  ░           ░  ░   ░        ░  ░
''', 'blue')
BANNER2 = colored('''                                    RARNinja: The RAR Password Cracking Utility''', 'red')
BANNER3 = colored('''                                   ---------------------------------------------''', 'blue')


def printBanner():
    init()
    print(BANNER1), print(BANNER2), print(BANNER3)


def progress():
    found = False
    with open(dictionary, "r") as file:
        for line in enumerate(file):
            password = str(line[1]).strip()
            try:
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                    print(f"\nCracked and extracted! Password: {password}")
                    found = True
                    break
            except:
                print(f"Incorrect password used: {password}")
                continue
    return(found, line[0])


def noProgress():
    found = False
    print("\nWorking...", end='')
    with open(dictionary, "r") as file:
        for line in enumerate(file):
            password = str(line[1]).strip()
            try:
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                    print(f"\n\nCracked and extracted! Password: {password}")
                    found = True
                    break
            except:
                continue
    return(found, line[0])


####### Main #######

if __name__ == "__main__":

    printBanner()

    while (correctPath is False):
        try:
            RAR = input("Enter RAR file path here: ")
            dictionary = input("Enter dictionary file path here: ")

            open(dictionary, "r")
            open(RAR, "r")

            print("\nShow progress?")
            print("1. Yes (slower)\n2. No (faster)")
            progressPrompt = int(input("\nSelect option number (Default = No): ") or 2)

        except FileNotFoundError:
            print("\nEither file does not exist or invalid path entered. Try again.\n")
            continue

    if (progressPrompt == 1):
        start = time.time()
        found, tries = progress(dictionary, RAR)
        completionTime = time.time() - start
    elif (progressPrompt == 2):
        start = time.time()
        found, tries = noProgress(dictionary, RAR)
        completionTime = time.time() - start
    try:
        rate = (int(tries) // completionTime)

        if found:
            print(f"\n\nThe task completed successfully in {completionTime} seconds. (at ~{rate} tries/sec)")
            print("Press any key to exit.")
            input()
        else:
            print(f"\n\nAll lines in {dictionary} tried and exhausted, password not found. You may try another dictionary file.")
            print("Press any key to exit.")
            input()
    except ZeroDivisionError:
        print("\n\nThe task completed successfully in zero seconds.")
        print("Press any key to exit.")
        input()
