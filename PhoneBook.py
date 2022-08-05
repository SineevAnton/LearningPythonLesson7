
def DeleteContact():
    # This method will delete contact by surname from the phone book.
    # If there are more than one record with same surname - all of this records
    # will be show to user to let him choose only one of them.

    def deleteRowData(data, dataToDelete):
        if dataToDelete[0] in data:
            data.remove(dataToDelete[0])
        return "".join(data)

    def deleteColumnData(data, dataToDelete):
        result = []
        correctedData = [el for el in dataToDelete[0].split(',')]
        for i in range(3):
            correctedData[i] = correctedData[i] + '\n'
        for i in range(0, len(data), 4):
            if (correctedData[0] == data[i]) and (correctedData[1] == data[i + 1]) and (
                    correctedData[2] == data[i + 2]) and (correctedData[3] == data[i + 3]):
                # data.remove(data[i])
                # data.remove(data[i+1])
                # data.remove(data[i+2])
                # data.remove(data[i+3])
                continue
            else:
                result.append(data[i])
                result.append(data[i + 1])
                result.append(data[i + 2])
                result.append(data[i + 3])
        return "".join(result)

    surnameToDelete = input('Please enter surname of contact to delete the record: ')

    rowData = []
    columnData = []

    with open('dataFormatRow.txt', 'r', encoding='utf-8') as dataFile:
        rowData = dataFile.readlines()
    with open('dataFormatColumn.txt', 'r', encoding='utf-8') as dataFile:
        columnData = dataFile.readlines()

    dataToDelete = []
    for el in rowData:
        if surnameToDelete in el:
            dataToDelete.append(el)

    if len(dataToDelete) == 0:
        print("Contact didn't found. Try again.")
    elif len(dataToDelete) == 1:
        with open('dataFormatRow.txt', 'w', encoding='utf-8') as dataFile:
            dataFile.write(deleteRowData(rowData, dataToDelete))
        with open('dataFormatColumn.txt', 'w', encoding='utf-8') as dataFile:
            dataFile.write(deleteColumnData(columnData, dataToDelete))
    else:
        counter = 0
        for el in dataToDelete:
            print(f'{counter}: {el}', end='')
            counter += 1

        while True:
            rowNumber = int(input('Please select the number of the row u want to delete: '))
            if rowNumber >= 0 and rowNumber < len(dataToDelete):
                break
            else:
                print('Incorrect input. Please, Try again.')

        with open('dataFormatRow.txt', 'w', encoding='utf-8') as dataFile:
            dataFile.write(deleteRowData(rowData, [dataToDelete[rowNumber]]))
        with open('dataFormatColumn.txt', 'w', encoding='utf-8') as dataFile:
            dataFile.write(deleteColumnData(columnData, [dataToDelete[rowNumber]]))

def AddContact():
    # This method will add contact to the phone book, using both data format.
    # Despite of user choice of data format - method add data to both .txt files.

    pathFormatColumn = 'dataFormatColumn.txt'
    pathFormatRow = 'dataFormatRow.txt'

    def getContactData():
        data = []
        data.append(input('Please, enter contact surname: '))
        data.append(input('Please, enter contact name: '))
        data.append(input('Please, enter contact phone: '))
        data.append(input('Please, enter contact description: '))

        return data

    data = getContactData()
    dataStringRow = ",".join(data)
    dataStringColumn = "\n".join(data)

    with open(pathFormatRow, 'a', encoding='utf-8') as rowFile:
        rowFile.write(dataStringRow + '\n')

    with open(pathFormatColumn, 'a', encoding='utf-8') as columnFile:
        columnFile.write(dataStringColumn + '\n')

def SearchContact():
    # Function to search contact by it's name.
    # If there ar more than one contact with searching name - all of them will ba displayed.

    nameToSearch = input('Please enter the name to search: ')

    data = []
    with open('dataFormatRow.txt', 'r', encoding='utf-8') as dataFile:
        data = dataFile.readlines()

    searchResult = []

    for el in data:
        if nameToSearch == el.split(',')[1]:
            searchResult.append(el)

    if len(searchResult) == 0:
        print('Contact not found.')
    else:
        for el in searchResult:
            print(el, end="")

def chooseFormatStile():
    # Function to choose the kind of data format: as a row or as a column.

    #def chooseFormatStile():
        print('Do u wanna see data as a row or as a column?')
        print('Example:')
        print('Row (chose "r" or "R"):\nSurname_1,Name_1,Phone_1,Description_1')
        print('Column (chose "c" or "C"):\nSurname_1\nName_1\nPhone_1\nDescription_1')
        while True:
            choice = input('Please enter "c" or "r": ')
            if choice not in "cCrR":
                print('Error! Only letters "c" ("C") or "r" ("R") allowed!')
            else:
                if choice in "cC":
                    mainPath = 'dataFormatColumn.txt'
                    secondPath = 'dataFormatRow.txt'
                else:
                    mainPath = 'dataFormatRow.txt'
                    secondPath = 'dataFormatColumn.txt'
                break
        return [mainPath, secondPath]

def ShowContacts():
    # This function will print phone book in console, using data format, determining in 'SelectDataFormat'
    pathList = chooseFormatStile()

    data = []
    with open(pathList[0], 'r', encoding='utf-8') as dataFile:
        data = dataFile.readlines()

    print()
    print('Contacts:')
    for el in data:
        print(el, end="")

def phoneBookStartApp():

    while True:
        print('Hi, user! This is Your phone book.')
        print('What do u wanna do?')
        print('1. Show contacts.')
        print('2. Search contact.')
        print('3. Add contact.')
        print('4. Delete contact.')
        print('5. Close program.')

        while True:
            userChoice = int(input('Please enter a number from 1 to 5: '))
            if str(userChoice) not in "12345":
                print('Incorrect input.')
            else:
                break
        if userChoice == 5:
            break
        else:

            if userChoice == 1:
                ShowContacts()
            elif userChoice == 2:
                SearchContact()
            elif userChoice == 3:
                AddContact()
            elif userChoice == 4:
                DeleteContact()


            # actionList = [ShowContacts(), SearchContact(), AddContact(),DeleteContact()]
            # actionList[userChoice - 1]

phoneBookStartApp()