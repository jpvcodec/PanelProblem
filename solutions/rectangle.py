def dataValidation(data):
    try:
        intData = int(data)
    except ValueError:
        return False, "El dato debe ser un número, intente nuevamente: "
    if intData > 0:
        return True, "-"
    else: 
        return False, "El dato debe ser un número mayor a 0, intente nuevamente: "
    
def dataInput():
    values = [0, 0, 0, 0]
    mssgs = ["Indique el ancho X de la superficie: ", 
              "Indique el alto Y de la superficie: ",
              "Indique el ancho A de la baldosa: ",
              "Indique el alto B de la baldosa: "]
    i = 0
    for inputMssg in mssgs:
        val = input(inputMssg)
        valid, mssg = dataValidation(val)
        while not valid:
            val = input(mssg)
            valid, mssg = dataValidation(val)
        values[i] = int(val)
        i = i + 1
    return values[0], values[1], values[2], values[3]

def numSeparator(num):
    intPart = int(num)
    decPart = num % 1
    return intPart, decPart

def fill(x, y, a, b):
    intX, decX = numSeparator(x/a)
    intY, decY = numSeparator(y/b)
    intExtraX = 0
    intExtraY = 0
    if decX > 0:
        remainingSpace = x - (a*intX)
        if remainingSpace >= b:
            intExtraX, _ = numSeparator(y/a)
    if decY > 0:
        remainingSpace = y - (b*intY)
        if remainingSpace >= a:
            intExtraY, _ = numSeparator(x/b)
    return intX * intY + intExtraX + intExtraY
    
def solve(x, y, a, b):
    return max(fill(x, y, a, b), fill(x, y, b, a))

exit = False
while not exit:
    x, y, a, b = dataInput()
    print("El número de baldosas es: " + str(solve(x, y, a, b)))
    continueInput = input("Ingrese cualquier mensaje para continuar. Ingrese 0 para salir ")
    if continueInput == "0":
        exit = True