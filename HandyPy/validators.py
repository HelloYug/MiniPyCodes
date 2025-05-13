#  InputData --> Asks for input till getting desired datatype

def InputData(ToVerify, DataType, ErrorType, AskTimes, ErrorMessage = "\nEnter a Valid input!", ErrorCaseInput = "Enter data: "):
    '''
    ***Use this to copy the code, not to use as function***\n\n

    This function asks for Input till it gets desired type of input.\n
    returns the data in desired datatype or will asked for \n\n
    \n
    Arguments Info;\n
    \tToVerify --> Input to get of desired datatype.\n
    \tDataType --> Desired Data Type of input.\n
    \tErrorType --> ErrorType faced while getting desired datatype.\n
    \tAskTimes --> This no. of times system will ask for input if desired datatype not found.\n
    \tErrorMessage --> If desired datatype not found this message will me shown as errormessage. (Default: \\nEnter a Valid input!)\n
    \tErrorCaseInput --> If desired datatype not found the input asked message will be this. (Default: Enter data: )
    '''
    
    cnt = 0
    while True:
        try:
            DataType (RepeatToVerify)
            if type (ToVerify) == DataType:
                break
            
        except ErrorType:
            print (ErrorMessage)
            RepeatToVerify = input (ErrorCaseInput)

        if cnt == AskTimes:
            break

        cnt += 1

    return RepeatToVerify