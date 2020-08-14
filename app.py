import random

def main():
    loop = True

    while loop:
        print('-----------------------------------')
        doors = [False, False, False]
        correct = random.randint(0, 2)
        doors[correct] = True

        choice = int(input("select one option [0, 1, 2]: "))
        print('Your choice: {}'.format(choice))

        r = random.randint(0, 1000)
        if bool(r % 2):
            for index in range(len(doors)):
                if doors[index] == False and index != choice:
                    print('At door {} there is a goat'.format(index))
                    break
        else:
            reversed_doors = doors
            reversed_doors.reverse()
            for index in range(len(reversed_doors)):
                if doors[index] == False and index != choice:
                    print('At door {} there is a goat'.format(index))
                    break

        choice = int(input("Do you want to choose other door? "))


        if choice == correct:
            print('You win, correct answer is: {}, {}'.format(correct, doors))
        else:
            print('You lose, correct answer is: {}, {}'.format(correct, doors))

        loop = bool(int(input("keep in the game?, [0, 1] ")))


if __name__ == '__main__':
    main()
