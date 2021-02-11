import datetime
def gettime():
    return datetime.datetime.now()

# taking tasks
def take(family_member):
    if (family_member==1):
        exercise_lock = int(input("Enter 1 for exercise and 2 for food"))
        if(exercise_lock==1):
            value = input("Enter Dad's Exercise in a day:\n")
            with open("dad_exercise.txt","a") as op:
                op.write(str([str(gettime())])+":" + value + "\n")
            print("Successfully Written")

        elif(exercise_lock==2):
            value = input("Enter the food that must be consumed by dad in a day:\n")
            with open("dad_food.txt","a") as op:
                op.write(str([str(gettime())]) + ":" + value +"\n")
                print("Successfully Written")
    elif(family_member==2):
        exercise_lock = int(input("Enter 1 for exercise and 2 for food"))
        if (exercise_lock==1):
            value = input("Enter Mom's Exercise  in  day:\n")
            with open("mom_exercise.txt","a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
                print("Successfully Written")


        elif (exercise_lock==2):
            value = input("Enter the food that must be consumed by mom in a day:\n")
            with open("mom_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
                print("Successfully Written")

    elif (family_member==3):
        exercise_lock = int(input("Enter 1 for exercise and 2 for food"))
        if (exercise_lock==1):
            value = input("Enter Brother's Exercise in  day:\n")
            with open("bro_exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
                print("Successfully Written")


        elif (exercise_lock==2):
            value = input("Enter the food that must be consumed by brother in a day:\n")
            with open("bro_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
                print("Successfully Written")


    elif (family_member==4):
        exercise_lock = int(input("Enter 1 for exercise and 2 for food"))
        if (exercise_lock==1):
            value = input("Enter Sister's Exercise  in  day:\n")
            with open("sis_exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
                print("Successfully Written")


        elif (exercise_lock==2):
            value = input("Enter the food that must be consumed by sis in a day:\n")
            with open("sis_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
                print("Successfully Written")


    elif (family_member==5):
        exercise_lock = int(input("Enter 1 for exercise and 2 for food"))
        if (exercise_lock==1):
            value = input("Enter Ana's Exercise in a day:\n")
            with open("Ana_exercise.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
                print("Successfully Written")


        elif (exercise_lock==2):
            value = input("Enter the food that must be consumed by Ana in a day:\n")
            with open("Ana_food.txt", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + "\n")
                print("Successfully Written")

        else:
            print("Please Enter valid input (1(dad), 2(mom), 3(bro), 4(sis), 5(ana)")


def retrive(family_member):
    if family_member==1:
        exercise_lock = int(input("Enter 1 For exercise and 2 for food"))
        if (exercise_lock==1):
            with open("dad_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif(exercise_lock==2):
            with open("dad_food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (family_member==2):
        exercise_lock = int(input("Enter 1 For exercise and 2 for food"))
        if (exercise_lock==1):
            with open("mom_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (exercise_lock == 2):
            with open("mom_food.txt") as op:
                for i in op:
                    print(i, end="")

    elif (family_member==3):
        exercise_lock = int(input("Enter 1 For exercise and 2 for food"))
        if (exercise_lock==1):
            with open("bro_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (exercise_lock == 2):
            with open("bro_food.txt") as op:
                for i in op:
                    print(i, end="")

    elif (family_member==4):
        exercise_lock = int(input("Enter 1 For exercise and 2 for food"))
        if (exercise_lock==1):
            with open("sis_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (exercise_lock == 2):
            with open("sis_food.txt") as op:
                for i in op:
                    print(i, end="")

    elif (family_member==5):
        exercise_lock = int(input("Enter 1 For exercise and 2 for food"))
        if (exercise_lock==1):
            with open("Ana_exercise.txt") as op:
                for i in op:
                    print(i, end="")
        elif (exercise_lock == 2):
            with open("Ana_food.txt") as op:
                for i in op:
                    print(i, end="")

    else:
        print("Please enter valid input (dad, mom, bro, sis, Ana)")
print("Health Management System Of a Family:")

options = int(input("Press 1 for lock and 2 for retrive"))

if options==1:
    family_member_name = int(input("Press 1 for dad, 2 for mom, 3 for bro, 4 for sis, 5 for Ana "))
    take(family_member_name)

else:
    family_member_name = int(input("Press 1 for dad, 2 for mom, 3 for bro, 4 for sis, 5 for Ana "))
    retrive(family_member_name)

