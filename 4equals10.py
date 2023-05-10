# Author = Akshat S.
# the code is build as a solution to a game 4 = 10.
# in this game 4 digits are given and we have to combine them using different operators.
# This code takes in those nubers, severable conditions that the game might throw at you. And provides a list of solutions

# tool helps in creating all the possible permutationsa and combinations of something
import itertools
import warnings  # gets rid of any syntax warnings that the system might return

# takes a list and returns a list, whose every element is also a list of numbers that is of all the possible permutations of the first list.
# example: if it takes [0,1,2], it returns [[0,1,2],[0,2,1],[1,2,0],[1,0,2],[2,0,1],[2,1,0]]


def order(num_list):
    full_num_list = []  # list where all the possible permutations will be stored

    # x is a tuple with a single permutation of the elements of the list
    for x in itertools.permutations(num_list):
        x = list(x)
        full_num_list.append(x)

    return full_num_list


def solve_with_br(full_num_list, no_sign_list):
    sol_list = []  # lists where all the solutions will be added
    sol_num = 0  # number of solutions will be added here
    oper_list = ["+", "-", "*", "/"]  # list of all the operations
    br_list = ['(', ')', '']  # list of all the brackets

    # loop will make sure if a sign cannot be used, it isn't used
    for s in no_sign_list:
        oper_list.remove(s)

    # each for loop will give 4 numbers, 3 operations, and 8 brackets. one element in the br_list is empty, which represents no brackets in that spot.
    # n is a list of one 1 permutation out of every single permutatin
    # o1, o2, o3 are 3 operations that will be in between 4 numbers
    # b1, b3, b4, b5, b6, b8 are 6 bracket operations on the front and back of the four numbers, expect at the back of first numbers and infront of the second number
        # because having brackets there will not make any sense. So, brackets b2 and b7 were omitted
    for n in full_num_list:
        for o1 in oper_list:
            for o2 in oper_list:
                for o3 in oper_list:
                    for b1 in br_list:
                        for b3 in br_list:
                            for b4 in br_list:
                                for b5 in br_list:
                                    for b6 in br_list:
                                        for b8 in br_list:
                                            
                                            # gets rid of all syntax warnings that might occur when evaluating the sum.
                                            warnings.filterwarnings('ignore')
                                            # PS: syntaxwarning are just warning and not syntaxerrors. They just show up and do nothing with the compilation.

                                            # combines all the numbers, operations and brackets in every possible combination.
                                            new_num = b1 + n[0] + " " + o1 + " " + b3 + n[1] + b4 + \
                                                " " + o2 + " " + b5 + \
                                                n[2] + b6 + " " + \
                                                o3 + " " + n[3] + b8

                                            # a and b count the number of open and closed parathesis in the above equation new_num
                                            a = new_num.count('(')
                                            b = new_num.count(')')

                                            # for every open parathesis, there is a closed parathesis and we can only have one bracket, So a = b = 1
                                            if a == b <= 1:
                                                try:
                                                    # eval function can take a list and convert it into amath equation that can be solved
                                                    sum = eval(new_num)
                                                except:
                                                    # if there is a bracket error, zero division error, then sum is impossible
                                                    sum = 'not possible'

                                                # uncomment this piece of code if you want to see all the possible combinations being calculated and taking
                                                # place, if brackets exist in the solution
                                                # if sum != 'not possible':
                                                #     print(new_num, end='')
                                                #     print(" = ", sum)

                                                # append the solution list and number of solution
                                                if sum == 10:
                                                    sol_list.append(new_num)
                                                    sol_num += 1
    return(sol_list, sol_num)


def solve(full_num_list, no_sign_list):
    sol_list = []  # lists where all the solutions will be added
    sol_num = 0  # number of solutions will be added here
    oper_list = ["+", "-", "*", "/"]  # list of all the operations

    # loop will make sure if a sign cannot be used, it isn't used
    for s in no_sign_list:
        oper_list.remove(s)

    # each for loop will give 4 numbers, 3 operations, and 8 brackets. one element in the br_list is empty, which represents no brackets in that spot.
    # n is a list of one 1 permutation out of every single permutatin
    # o1, o2, o3 are 3 operations that will be in between 4 numbers
    for n in full_num_list:
        for o1 in oper_list:
            for o2 in oper_list:
                for o3 in oper_list:
                    # gets rid of all syntax warnings that might occur when evaluating the sum.
                    warnings.filterwarnings('ignore')
                    # PS: syntaxwarning are just warning and not syntaxerrors. They just show up and do nothing with the compilation.

                    # combines all the numbers, operations and brackets in every possible combination.
                    new_num = n[0] + " " + o1 + " " + n[1] + " " + o2 + " " + n[2] + " " + o3 + " " + n[3]
                    # print(new_num, end = '')
                    try:
                        # eval function can take a list and convert it into amath equation that can be solved
                        sum = eval(new_num)
                        # print('=', sum)
                        
                    except:
                        # if there is a bracket error, zero division error, then sum is impossible
                        sum = 'not possible'

                        # uncomment this piece of code if you want to see all the possible combinations being calculated and taking
                        # place, if brackets donot exist in the solution
                        # if sum != 'not possible':
                        # print(new_num, end='')
                        # print(" = ", sum)

                        # append the solution list and number of solution
                        if sum == 10:
                            sol_list.append(new_num)
                            sol_num += 1
                            
    return(sol_list, sol_num)


def main():
    # takes the number from the user as a 4 character string
    number = input("enter your numbers: ")

    # make sure that user inputs the right amount of numbers.
    while len(number) != 4:
        print('Please enter 4 digits, without using any spaces or commas')
        number = input("enter your numbers: ")

    # takes the signs from the user that cannot be used in the string
    sign = input("enter the signs that you can't use: ")
    sign = list(sign)
    # list of all the operations
    sign_list = ["+", "-", "*", "/", "(", ")", ""]
    k = True

    for i in sign:
        if i not in sign_list:
            k = False
        else:
            k = True

    while k == False:
        print("please only enter signs, ie '+' for additions, '-' for subtraction, '*' for multiplication, '/' for division, '()' for opening and closing pranthesis, without any spaces, commas or quotation marks")
        sign = input("enter the signs that you can't use: ")
        k = True
        for i in sign:
            print(i)
            if i not in sign_list:
                k = False
            else:
                k = True

    # asks if we should use brackets or not
    br = input("with brackets (y/n): ")

    # makes sure that the br is only answered with a yes or a know
    while br != 'n' and br != 'y':
        print("only answer as 'y' or 'n'. Asnswer 'y', if you want us to use brackets, answer 'n' if you don't wnat us to use brackets in your answer. ")
        br = input("with brackets (y/n): ")

    # makes a list of numbers.
    number = list(number)

    # calls the function that makes list of all permutations of the given list.
    full_num_list = order(number)

    # if we don't need brackets
    if br == 'n':
        # calls the functions that creates a solution list and finds number of solutions that exist.
        solution, num = solve(full_num_list, sign)

        # if number of solutions are zero, then it will print that no solutions exist
        if num == 0:
            print('There are no solutions. Too bad.')

        # if number of solutions are not zero, then it will print how many solutions their are and prints a list of all the solutions
        else:
            print("We have found", num, "solutions, which are as follow: ")
            for i in solution:
                print(i)

    # if we do need brackets
    elif br == 'y':
        # calls the functions that creates a solution list and finds number of solutions that exist.
        solution, num = solve_with_br(full_num_list, sign)

        # if number of solutions are zero, then it will print that no solutions exist
        if num == 0:
            print('There are no solutions. Too bad.')

        # if number of solutions are not zero, then it will print how many solutions their are and prints a list of all the solutions
        else:
            print("We have found", num, "solutions, which are as follow: ")
            for i in solution:
                print(i)


if __name__ == '__main__':
    main()
