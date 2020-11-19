import random


print("----- Поле чудес -----")
print("0. Выйти из игры")
print("1. Начать игру")

sosi = False
balance = 0
points = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, "Приз", "+", "x2", "Банкрот"]
a = int(input("Выберите: "))
vopros = random.randrange(0,9,2)
words = open("words.txt", "r", encoding="utf8")
nums = words.read().splitlines()
words.close()
listLetters = list("_"*len(nums[vopros+1]))

if a == 1:
    while 1:        
        
        if sosi == True:
            vopros = random.randrange(0,9,2)
            listLetters = list("_"*len(nums[vopros+1]))
            sosi = False

        listwords = list(nums[vopros+1])
        print(nums[vopros]+"\n")
        
        print(str(len(nums[vopros+1]))+" букв: "+str(listLetters))
        print("\n---крутится барабан---")
        point = str(points[random.randint(0, 14)])
        print("сектор "+point +" на барабане!")
        
            
        if point == "Приз":
            print("Вы выйграли приз")
            
        elif point == "+":
            print("Вы можете открыть букву")
            pass
        elif point == "x2":
            print("Ваши очки удвоены на 2")
            balance *= 2
            
        elif point == "Банкрот":
            print("Вы банкрот")
            balance = 0
            
        elif int(point) in points[:-4] and int(point)!=0:
            balance += int(point)
            print("У вас "+str(balance)+" очков")            
            
        letter = input("Введите букву: ")
        for i in range(len(listwords)):
            if letter==listwords[i]:
                print("Есть такая буква!")
                listLetters[i] = letter
                if i == len(listwords):
                    break
            else: 
                continue
        myString = ''.join(listLetters)
        if myString == nums[vopros+1]:
            print("\n"+str(len(nums[vopros+1]))+" букв: "+str(listLetters))
            print("Вы выиграли!")
            sosi = True
            print("Что хотите сделать дальше")
            print("0. Выйти из игры")
            print("1. Продолжить игру")
            sosi2 = int(input())
            if sosi2 == 0:
                break
            elif sosi2 == 1:
                continue
elif a == 0:
    print("Конец игры")


