#day2

def loader(file):
    '''loads numbers from inputfile'''

    with open(file) as rawfile:
        data = rawfile.read()
        return data


def day_2_solve1(data):
    '''solves first puzzle'''

    data = [[int(numbers) for numbers in row.split()] for row in data.splitlines()]
    checksum = 0

    for row in data:
        checksum += (max(row) - min(row))

    print("The solution is:", checksum)

day_2_solve1(loader("day2.txt"))