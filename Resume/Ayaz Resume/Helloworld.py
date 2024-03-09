

def Max_Digit(List):
    inital_Digit = List[0]
    for number in List:
        if inital_Digit < number:
            inital_Digit = number
    return inital_Digit