filename = open('data.txt')
lines = filename.readlines()
stringToNumberDict = {
    'one': 1, 
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}
def processDataAndSaveToList(data):
    firstDigit = ""
    lastDigit = ""
    for i in data:
        if i.isdigit() or matchTextToNumber(i, data) is not None:
            lastDigit = i
            if firstDigit == "":
                firstDigit = i
    if firstDigit != "" and lastDigit != "":   
        twoDigits = firstDigit + lastDigit
        numberList.append(int(twoDigits))
    return numberList

def matchTextToNumber(char, string):
    matchingKey = [key for key in stringToNumberDict if key.startswith(char.lower())]

    for key in matchingKey:
        if string.lower().startswith(key[1:]):
            return stringToNumberDict
    return None
#Seems like valid text to int is not happening so check that
numberList = []

for data in lines:
    processDataAndSaveToList(data)

caliberationValue = sum(numberList)

print(caliberationValue)