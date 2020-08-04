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


def progress(dictionary, RAR):
    found = False
    with open(dictionary, 'r') as file:
        for line in enumerate(file):
            password = str(line[1]).strip()
            try:
                with rarfile.RarFile(RAR, 'r') as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                    print("\nCracked and extracted! Password: " + password)
                    found = True
                    break
            except:
                print("Incorrect password used: " + password)
                continue
    return(found, line[0])


def noProgress(dictionary, RAR):
    found = False
    print("\nWorking...", end='')
    with open(dictionary, 'r') as file:
        for line in enumerate(file):
            password = str(line[1]).strip()
            try:
                with rarfile.RarFile(RAR, 'r') as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                    print("\n\nCracked and extracted! Password: " + password)
                    found = True
                    break
            except:
                continue
    return(found, line[0])


def prompt():
    while (correctPath is False):
        try:
            RAR = input("Enter RAR file path here: ")
            dictionary = input("Enter dictionary file path here: ")

            open(dictionary, 'r')
            open(RAR, 'r')

            print("\nShow progress?")
            print("1. Yes (slower)\n2. No (faster)")
            progressPrompt = input("\nSelect option number (Default = No): ") or "2"

            if (progressPrompt in ["1", "2"]):
                return(dictionary, RAR, progressPrompt)
            else:
                print("\nInvalid option number entered. Try again.\n")
                continue
        except FileNotFoundError:
            print("\nEither file does not exist or invalid path entered. Try again.\n")
            continue


####### Main #######

if __name__ == "__main__":

    printBanner()

    dictionary, RAR, progressPrompt = prompt()

    if (progressPrompt == "1"):
        start = time.time()
        found, tries = progress(dictionary, RAR)
        completionTime = time.time() - start
    elif (progressPrompt == "2"):
        start = time.time()
        found, tries = noProgress(dictionary, RAR)
        completionTime = time.time() - start

    rate = (int(tries) // completionTime)

    if found:
        print("\n\nThe task completed successfully in %f seconds. (at ~%d tries/sec)" % (completionTime, rate))
        print("Press any key to exit.")
        input()
    else:
        print("\n\nAll lines in " + dictionary + " tried and exhausted, password not found. You may try another dictionary file.")
        print("Press any key to exit.")
        input()
