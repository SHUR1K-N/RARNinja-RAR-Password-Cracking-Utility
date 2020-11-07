import rarfile; import threading
import time; import os
from termcolor import colored
import colorama

colorama.init()

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
     ░           ░  ░   ░              ░  ░           ░  ░   ░        ░  ░''', 'blue')
BANNER2 = colored('''             -------------------------------------------------''', 'blue')
BANNER3 = colored('''             || RARNinja: The RAR Password Cracking Utility ||''', 'red')
BANNER4 = colored('''             -------------------------------------------------''', 'blue')


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3), print(BANNER4)


def generator():
    with open(dictionary, "r") as file:
        for line in file:
            yield line.strip()


class AttackFunctions:

    def attackRAR1(passwordList, chunkOne):
        for password in passwordList[0:chunkOne]:
            try:
                # print(password)
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                clrscr()
                print(colored(f"\nPassword found! Password: {password}", "green"))
                print("\nYou may now exit this window.")
                input()
            except:
                continue

    def attackRAR2(passwordList, chunkOne, chunkTwo):
        for password in passwordList[chunkTwo - 1:chunkOne - 1:-1]:
            try:
                # print(password)
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                clrscr()
                print(colored(f"\nPassword found! Password: {password}", "green"))
                print("\nYou may now exit this window.")
                input()
            except:
                continue

    def attackRAR3(passwordList, chunkTwo, chunkThree):
        for password in passwordList[chunkTwo:chunkThree]:
            try:
                # print(password)
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                clrscr()
                print(colored(f"\nPassword found! Password: {password}", "green"))
                print("\nYou may now exit this window.")
                input()
            except:
                continue

    def attackRAR4(passwordList, chunkThree, chunkFour):
        for password in passwordList[chunkFour - 1:chunkThree - 1:-1]:
            try:
                # print(password)
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                clrscr()
                print(colored(f"\nPassword found! Password: {password}", "green"))
                print("\nYou may now exit this window.")
                input()
            except:
                continue

    def attackRAR5(passwordList, chunkFour, chunkFive):
        for password in passwordList[chunkFour:chunkFive]:
            try:
                # print(password)
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                clrscr()
                print(colored(f"\nPassword found! Password: {password}", "green"))
                print("\nYou may now exit this window.")
                input()
            except:
                continue

    def attackRAR6(passwordList, chunkFive, chunkSix):
        for password in passwordList[chunkSix - 1:chunkFive - 1:-1]:
            try:
                # print(password)
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                clrscr()
                print(colored(f"\nPassword found! Password: {password}", "green"))
                print("\nYou may now exit this window.")
                input()
            except:
                continue

    def attackRAR7(passwordList, chunkSix, chunkSeven):
        for password in passwordList[chunkSix:chunkSeven]:
            try:
                # print(password)
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                clrscr()
                print(colored(f"\nPassword found! Password: {password}", "green"))
                print("\nYou may now exit this window.")
                input()
            except:
                continue

    def attackRAR8(passwordList, chunkSeven):
        for password in passwordList[:chunkSeven - 1:-1]:
            try:
                # print(password)
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(path="./Extracted/", pwd=password)
                clrscr()
                print(colored(f"\nPassword found! Password: {password}", "green"))
                print("\nYou may now exit this window.")
                input()
            except:
                continue


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


############### Main ###############

if __name__ == "__main__":

    printBanner()

    try:

        while (True):
            RAR = input("\nEnter RAR file path here: ")
            dictionary = input("Enter dictionary file path here: ")

            if (os.path.isfile(RAR) is True and os.path.isfile(dictionary) is True):
                break
            else:
                clrscr()
                print("\nEither file does not exist or invalid path entered. Try again.\n")
                continue

        generatedList = generator()
        passwordList = list(generatedList)

        chunkOne = len(passwordList) // 8
        chunkTwo = chunkOne * 2
        chunkThree = chunkOne * 3
        chunkFour = chunkOne * 4
        chunkFive = chunkOne * 5
        chunkSix = chunkOne * 6
        chunkSeven = chunkOne * 7

        threadForwardOne = threading.Thread(target=AttackFunctions.attackRAR1, args=[passwordList, chunkOne])
        threadReverseOne = threading.Thread(target=AttackFunctions.attackRAR2, args=[passwordList, chunkOne, chunkTwo])

        threadForwardTwo = threading.Thread(target=AttackFunctions.attackRAR3, args=[passwordList, chunkTwo, chunkThree])
        threadReverseTwo = threading.Thread(target=AttackFunctions.attackRAR4, args=[passwordList, chunkThree, chunkFour])

        threadForwardThree = threading.Thread(target=AttackFunctions.attackRAR5, args=[passwordList, chunkFour, chunkFive])
        threadReverseThree = threading.Thread(target=AttackFunctions.attackRAR6, args=[passwordList, chunkFive, chunkSix])

        threadForwardFour = threading.Thread(target=AttackFunctions.attackRAR7, args=[passwordList, chunkSix, chunkSeven])
        threadReverseFour = threading.Thread(target=AttackFunctions.attackRAR8, args=[passwordList, chunkSeven])

        clrscr()
        print("\nWorking...", end="")

        threadPool = [threadForwardOne, threadReverseOne, threadForwardTwo, threadReverseTwo,
                      threadForwardThree, threadReverseThree, threadForwardFour, threadReverseFour]

        for thread in threadPool:
            thread.start()

        for thread in threadPool:
            thread.join()

    except KeyboardInterrupt:
        clrscr()
        print("\nCTRL ^C\n\nThrew a wrench in the works.")
        print("Press Enter to exit.")
        input()
