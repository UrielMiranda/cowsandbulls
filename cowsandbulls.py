import random


def generate_digit():
        cows = 0
        bulls = 0
        numRandom = str(random.randint(1000, 9999))
        print("\nRandom: ", numRandom)
        numUser = input("Numero de 4 digitos\n")
        print("\nUser: ", numRandom)
        print("Random: ", numUser)
        for digit in numRandom:
            print("Este es el valor de digit", digit)
            for num in numUser:
                if(num == digit):
                    bulls += 1
            print("Este es el valor de num", numUser)

        # print("\nRandom: ",numRandom)
        # print("User: ",numUser)
        print("\nTienes ", cows, " cows y ", bulls, " bulls")


# def check(index1,value1,index2,value2):
#     if(value1 == value2):
#         if(index1 == index2):
#             return cow += 1


def travel(elem, element):

    for ele in element
    pass


# generate_digit()
