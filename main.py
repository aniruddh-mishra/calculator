def solve(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        result = num1/num2
    elif operator == "*":
        result = num1*num2
    elif operator == "^":
        result = num1 ** num2
    return result

def calculate(cont, val=0):
    if not cont:
        while True:
            try:
                num1 = int(input("Enter the first number: "))
                break
            except:
                print("This value needs to be a number")
    else:
        num1 = val

    while True:
        try:
            if cont:
                num2 = int(input("Enter next number: "))
            else:
                num2 = int(input("Enter the second number: "))
                break
        except:
            print("This value needs to be a number")
    while True:
        operation = input("Enter the operator (+, -, /, *, ^): ")
        if operation not in "+-/*^":
            print("Your operation must be of the following: +, -, /, *, ^")
        else:
            break
    result = solve(num1, num2, operation)
    print(num1, operation, num2, "=", result)
    return result

def normalCalculator():
    result = calculate(False)
    while True:
        cont = input("Do you want to continue the calculation (y/N)? ")
        if cont != "y" and cont != "Y":
            break
    result = calculate(True, result)

def backSearchNum(expression, index):
    num = ""
    while index >= 0:
        index -= 1
        if index >= 0 and expression[index] in "0123456789.":
            num = expression[index] + num
        elif index == 0 and expression[index] == "-":
            num = expression[index] + num
        else:
            break

    return num

def forwardSearchNum(expression, index):
    num = ""
    if expression[index + 1] == "-":
        num = "-"
        index += 1

    while index < len(expression):
        index += 1
        if index < len(expression) and expression[index] in "0123456789.":
            num = num + expression[index]
        elif index == 0 and expression[index] == "-":
            num = num + expression[index]
        else:
            break
    
    return num

def pemdas(expression, operators):
    index = 0
    while index < len(expression):
        letter = expression[index]
        if letter in operators:
            num1 = backSearchNum(expression, index)
            if letter == "-" and num1 == "":
                expression = expression[:index] + "0" + expression[index:]
                continue
            num2 = forwardSearchNum(expression, index)
            value = solve(float(num1), float(num2), letter)
            expression = expression[:index - len(num1)] + str(value) + expression[index + 1 + len(num2):]
            index = index - len(num1) + len(str(value)) - 1
        index += 1
    return expression

def eval(expression):
    returnVal = 0
    operators = ["^", "/*", "-+"]
    for operatorSet in operators:
        expression = pemdas(expression, operatorSet)

    return expression

def parseExpression(expression):
    expression = " ".join(expression.split())
    expression = expression.replace(" ", "")
    base = True
    start = 0
    end = 0
    counter = 0
    operators = "^+-/*"
    if expression.count("(") != expression.count(")"):
        raise Exception()

    index = -1
    while index < len(expression) - 1:
        index += 1
        letter = expression[index]
        if letter == "(":
            counter += 1
            if base:
                base = False
                start = index
        elif letter == ")":
            counter -= 1
            if not counter and not base:
                end = index
                replaceVal = parseExpression(expression[start+1: end])
                if start == 0 or expression[start - 1] in operators:
                    expression = expression[:start] + str(replaceVal) + expression[end + 1:]
                else:
                    expression = expression[:start] + "*" + str(replaceVal) + expression[end + 1:]
                base = True
                index = start + len(str(replaceVal)) - 1

    if expression[0] == "*":
        expression = expression[1:]

    if base:
        return eval(expression)
    
def advancedCalculator():
    expression = input("Type in a calculation to complete. You may use operations (+, -, /, *, ^). This result will follow PEMDAS. (eg. (3 + 2 * 3)(4^2) = 144.0\n")
    try:
        print(expression, "=", str(parseExpression(expression)))
    except:
        print("Something went wrong. Please make sure that expression is correct. (eg. Same number of opening and closing parantheses or number may be too big)")

if __name__ == "__main__":
    while True:
        while True:
            option = input("Advanced (A) or Normal (N) calculator? ")
            if option not in "AaNn":
                print("You need to choose either A for Advanced or N for Normal")
            else:
                break

        if option == "A" or option == "a":
            advancedCalculator()
        else:
            normalCalculator()
            
        cont = input("Do you want to do another calculation (y/N)? ")
        if cont != "y" and cont != "Y":
            break