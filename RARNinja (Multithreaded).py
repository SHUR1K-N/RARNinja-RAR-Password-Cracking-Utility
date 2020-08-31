import rarfile; import time
import threading; import os
import winsound

rarfile.UNRAR_TOOL = "UnRAR.exe"


def generator():
    with open(dictionary, "r") as file:
        for line in enumerate(file):
            yield line[1].strip()


class AttackFunctions:

    def attackRAR1(passwordList, chunkOne):
        for password in passwordList[0:chunkOne]:
            try:
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(pwd=password)
                    print(f"\n\nPassword found! Password: {password}")
                    print("You may now exit this window.")
            except:
                continue

    def attackRAR2(passwordList, chunkOne, chunkTwo):
        for password in passwordList[chunkTwo - 1:chunkOne - 1:-1]:
            try:
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(pwd=password)
                    print(f"\n\nPassword found! Password: {password}")
                    print("You may now exit this window.")
            except:
                continue

    def attackRAR3(passwordList, chunkTwo, chunkThree):
        for password in passwordList[chunkTwo:chunkThree]:
            try:
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(pwd=password)
                    print(f"\n\nPassword found! Password: {password}")
                    print("You may now exit this window.")
            except:
                continue

    def attackRAR4(passwordList, chunkThree, chunkFour):
        for password in passwordList[chunkFour - 1:chunkThree - 1:-1]:
            try:
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(pwd=password)
                    print(f"\n\nPassword found! Password: {password}")
                    print("You may now exit this window.")
            except:
                continue

    def attackRAR5(passwordList, chunkFour, chunkFive):
        for password in passwordList[chunkFour:chunkFive]:
            try:
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(pwd=password)
                    print(f"\n\nPassword found! Password: {password}")
                    print("You may now exit this window.")
            except:
                continue

    def attackRAR6(passwordList, chunkFive, chunkSix):
        for password in passwordList[chunkSix - 1:chunkFive - 1:-1]:
            try:
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(pwd=password)
                    print(f"\n\nPassword found! Password: {password}")
                    print("You may now exit this window.")
            except:
                continue

    def attackRAR7(passwordList, chunkSix, chunkSeven):
        for password in passwordList[chunkSix:chunkSeven]:
            try:
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(pwd=password)
                    print(f"\n\nPassword found! Password: {password}")
                    print("You may now exit this window.")
            except:
                continue

    def attackRAR8(passwordList, chunkSeven):
        for password in passwordList[:chunkSeven - 1:-1]:
            try:
                with rarfile.RarFile(RAR, "r") as rar:
                    rar.extractall(pwd=password)
                    print(f"\n\nPassword found! Password: {password}")
                    print("You may now exit this window.")
            except:
                continue


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


####### Main #######

if __name__ == "__main__":

    RAR = input("\nEnter RAR file path here: ")
    dictionary = input("Enter dictionary file path here: ")

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

    threadForwardOne.start(), threadReverseOne.start()
    threadForwardTwo.start(), threadReverseTwo.start()
    threadForwardThree.start(), threadReverseThree.start()
    threadForwardFour.start(), threadReverseFour.start()

    threadForwardOne.join(), threadReverseOne.join()
    threadForwardTwo.join(), threadReverseTwo.join()
    threadForwardThree.join(), threadReverseThree.join()
    threadForwardFour.join(), threadReverseFour.join()
