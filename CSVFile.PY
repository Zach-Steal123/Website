def makeData():
    # Module Import(s)
    import csv
    import random
    # Variable(s)
    fileName = "PeopleAndweights.csv"
    header = ["Name", "Weight (kg)"]
    data = [
        ["Amanda", random.randint(1, 100)],
        ["Bob", random.randint(1, 100)],
        ["Charlotte", random.randint(1, 100)],
        ["David", random.randint(1, 100)],
        ["Emma", random.randint(1, 100)],
        ["Fionn", random.randint(1, 100)],
        ["Gretta", random.randint(1, 100)],
        ["Hector", random.randint(1, 100)],
        ["Ingrid", random.randint(1, 100)],
        ["John", random.randint(1, 100)],
        ["Katie", random.randint(1, 100)],
        ["Liam", random.randint(1, 100)],
        ["Molly", random.randint(1, 100)],
        ["Nathan", random.randint(1, 100)],
        ["Ophelia", random.randint(1, 100)],
        ["Patrick", random.randint(1, 100)],
        ["Quinn", random.randint(1, 100)],
        ["Robert", random.randint(1, 100)],
        ["Sophie", random.randint(1, 100)],
        ["Tom", random.randint(1, 100)],
        ["Ursula", random.randint(1, 100)],
        ["Victor", random.randint(1, 100)],
        ["Wendy", random.randint(1, 100)],
        ["Xander", random.randint(1, 100)],
        ["Yara", random.randint(1, 100)],
        ["Zach", random.randint(1, 100)]
    ]
    # Creating .CSV File
    with open(fileName, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
    # If File Works Message
    print(f'The file "{fileName}" has been created successfully')


makeData()
