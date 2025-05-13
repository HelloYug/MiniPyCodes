# GCD --> Calculates Greatest Common Factor of the given data list.
# LCM --> Calculates Least Common Multiple of the given data list.
# DecimalToFraction -->  Converts the given number value into fraction.
# DeciRange --> Returns a list of values of the range with step value as integer and float. Works exactly like range function but with float values as well.

def GCD (nums):
    '''
    Returns the Greatest Common Divisor as integer of the given list as nums and a nested list of all divisors of each number in the given list.\n
    nums --> list of numbers to find GCD of.\n
    returns a tuple --> (GCD, Nested list of factors of each number in sortrd given list)\n
    Example;\n
    \tFunc([10, 25, 20]) --> (5, [[1, 2, 5, 10],[1, 2, 4, 5, 10, 20],[1, 5, 25]])\n
    \tFunc([7, 20, 21]) --> (1, [[1, 7],[1, 2, 4, 5, 10, 20], [1, 3, 7, 21]])
    '''

    nums.sort()
    # Finding multiples
    listnums = []
    for GCD in nums:
        NumL = [1]

        for k in range (2, GCD+1):
            if GCD%k == 0:
                NumL.append (k)

        listnums.append (NumL)

    # making list of no. of multiples
    lennums = []
    for GCD in listnums:
        lennums.append (len (GCD))

    # Finding list with least elements and reversing it
    SmallIndexList = listnums [(lennums.index (min (lennums)))]
    SmallIndexListReverse = SmallIndexList[::-1]

    # Finding GCD
    for GCD in SmallIndexListReverse:
        cnt = 0
            
        for j in listnums:
            if GCD not in j:
                break

            cnt += 1
        
        if cnt == len(nums):
            break

    # returning output
    return GCD, listnums

def LCM (nums):
    '''
    Returns the Least Common Multiple as integer of the given list as nums and a nested list of all multiples of each number is given list upto LCM.\n
    nums --> list of numbers to find LCM of.\n
    returns a tuple --> (LCM, Nested list of multiples of each number in sortrd given list)\n
    Example;\n
    \tFunc([3, 5]) --> (15, [[3, 6, 9, 12, 15], [5, 10, 15]])\n
    \tFunc([15, 10, 20]) --> (60, [[10, 20, 30, 40, 50, 60], [15, 30, 45, 60], [20, 40, 60]])
    '''

    nums.sort()
    lcm = max (nums) # Fixing largest number as LCM for instance

    # Finding LCM
    while True:
        TempList = []
        for i in nums:
            TempList.append (lcm % i)
        
        flag = 1
        for i in TempList:
            if i != 0:
                flag = 0
                lcm += 1
                break

        if flag == 1:
            break

    # creating a list of all multiples till LCM
    AllMultiplesList = []
    for i in nums:
        MutliplesList= [i]
        digit = lcm//i

        for j in range (2, digit+1):
            MutliplesList.append (i*j)

        AllMultiplesList.append (MutliplesList)

    # returning Output
    return lcm, AllMultiplesList

def DecimalToFraction(Value):
    '''
    *** Pass Decimal or integer value only or face ValueError ***\n
    It returns the provided value into least reduced fraction form in string datatype.\n
    Parameter info; Value --> Float or integer value that needs to be converted into fraction\n
    Example;\n
    \tFunc(0.25) --> "1/4"\n
    \tFunc(2.52) --> "63/25"\n
    \tFunc(5.500) --> "11/2"\n
    \tFunc(6) --> "6/1"
    '''
    
    if (type(Value) == float) or (type(Value) == int):
        try:
            StrV = str (float (Value))
        except ValueError:
            pass

        # finding decimal place
        count = 0
        for i in StrV[::-1]:
            if i == ".":
                forward = int (StrV[StrV.index(".")+1:])
                break
            count += 1

        if forward != 0:
            # converting decimal to integer
            expo = 10**count
            if type (Value) != int:
                FullX = int (Value * expo)

            # provinding list of prime numbers to check for divisibility
            prime = [2,3,5,7,11,13,17,19,23,29,31,37,41]

            # main program (find least reduced fraction)
            frac = [FullX, expo]
            while True:
                flag = 0
                for i in prime:
                    if (frac[0]%i == 0) and (frac[1]%i == 0):
                        frac[0] = int(frac[0]/i)
                        frac[1] = int(frac[1]/i)
                        flag = 1
                        break

                if flag == 0:
                    break

            return f"{frac[0]} / {frac[1]}"

        else:
            return f"{Value} / 1"

    else:
        raise ValueError ("The argument is not a number!!!")
    
def DeciRange (a, b, Gap):
    '''
    Returns a list of values of the range with step value as integer and float.\n
    Works exactly like range function but with float values as well.\n
    Does not include upper limit.\n\n

    Arguments info;\n
    \ta --> start value\n
    \tb --> end value
    \tGap --> step value (can be decimal)\n\n
    
    Example;\n
    \tFunc(2, 3, 0.25) --> [2.0, 2.25, 2.5, 2.75]\n
    \tFunc(2, 3, 0.2) --> [2.0, 2.2, 2.4, 2.6, 2.8]\n
    \tFunc(2, 10, 2) --> [2.0, 4.0, 6.0, 8.0]
    '''

    # Finding the no. of digit to round of
    cnt = 0
    l = len (str (Gap))
    for i in str (Gap):
        if i == ".":
            break
        cnt += 1
    rou = l - cnt
    
    # Converting values to Float type
    a, b, Gap = float (a), float (b), float (Gap)
    Final =[]

    # Creating a list of values
    while a < b:
        print (round(a, rou))
        Final.append(round (a, rou))
        a += Gap

    flag = b
    if Gap < 0:
        flag = a
        
    # Handling a error
    if Final[-1] == flag:
        Final.remove(b)

    # Returning final list
    return Final