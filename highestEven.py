def isEven(num):
    return num % 2 == 0

def highestEven(li):
    '''
    Find and return the highest even number as defined in wikipdia https://simple.wikipedia.org/wiki/Even_number

    :param li: List of numbers
    :return: the highest even number
    '''
    ans = None
    for number in li:
        if isEven(number):
            if ans == None:
                ans = number
            if number > ans:
                ans = number
    return ans


test1 = highestEven([1, 2, 3, 4, 5])
test2 = highestEven([1, 2, 3, 4, 5, 6])
test3 = highestEven([1, 2, 3, 4, 5, -20])
test4 = highestEven([1.0, 2.0, 3.0, 4.5, 5])
test5 = highestEven([1, 3, 5])
test6 = highestEven([1, 2, 3, 4, 5, 5, 50])
test7 = highestEven([1, 7, 3, 5, -200])

print(test1 == 4)
print(test2 == 6)
print(test3 == 4)
print(test4 == 2)
print(test5 == None)
print(test6 == 50)
print(test7 == -200)