import rarfile; import time
from colorama import init
from termcolor import colored

correctPath = False

init()

print(colored('''
                         ██▀███   ▄▄▄       ██▀███   ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
                        ▓██ ▒ ██▒▒████▄    ▓██ ▒ ██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
                        ▓██ ░▄█ ▒▒██  ▀█▄  ▓██ ░▄█ ▒▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
                        ▒██▀▀█▄  ░██▄▄▄▄██ ▒██▀▀█▄  ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
                        ░██▓ ▒██▒ ▓█   ▓██▒░██▓ ▒██▒▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
                        ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
                          ░▒ ░ ▒░  ▒   ▒▒ ░  ░▒ ░ ▒░░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
                          ░░   ░   ░   ▒     ░░   ░    ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
                           ░           ░  ░   ░              ░  ░           ░  ░   ░        ░  ░
''', 'blue'))
print(colored('''                                    RARNinja: The RAR Password Cracking Utility''', 'red'))
print(colored('''                                   ---------------------------------------------''', 'blue'))

rarfile.UNRAR_TOOL = "UnRAR.exe"


def progress(dictionary, RAR):
    found = False
    with open(dictionary, 'r') as file:
        for line in file:
            password = line.strip()
            try:
                with rarfile.RarFile(RAR, 'r') as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                    print("Cracked and extracted! Password: " + password)
                    found = True
                    break
            except:
                print("Incorrect password used: " + password)
                continue
    return(found)


def noProgress(dictionary, RAR):
    found = False
    print("\nWorking...", end='')
    with open(dictionary, 'r') as file:
        for line in file:
            password = line.strip()
            try:
                with rarfile.RarFile(RAR, 'r') as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                    print(" Cracked and extracted! Password: " + password)
                    found = True
                    break
            except:
                continue
    return(found)


def prompt():
    while (correctPath is False):
        try:
            RAR = input("Supply RAR file path here: ")
            dictionary = input("Supply dictionary file path here: ")

            open(dictionary, 'r')
            open(RAR, 'r')

            print("\nShow progress?")
            print("1. Yes (slower)\n2. No (faster)")
            progressPrompt = input("\nSelect option number (Default = No): ") or "2"

            if (progressPrompt in ["1", "2"]):
                print(progressPrompt)
                return(dictionary, RAR, progressPrompt)
            else:
                print("\nInvalid option number entered. Try again.\n")
                continue
        except FileNotFoundError:
            print("\nEither file does not exist or invalid path entered. Try again.\n")
            continue


####### Main #######

dictionary, RAR, progressPrompt = prompt()

if (progressPrompt == "1"):
    start = time.time()
    found = progress(dictionary, RAR)
    completionTime = time.time() - start
elif (progressPrompt == "2"):
    start = time.time()
    found = noProgress(dictionary, RAR)
    completionTime = time.time() - start

if found:
    print("\n\nThe task completed successfully in %f seconds." % (completionTime))
    print("Press any key to exit.")
    input()
else:
    print("\n\nAll lines in " + dictionary + " tried and exhausted, password not found. You may try another dictionary file.")
    print("Press any key to exit.")
    input()
