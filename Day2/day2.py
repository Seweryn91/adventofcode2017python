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

    print("The solution 1 is:", checksum)
    
def day_2_solve2(data):
    '''solves second puzzle'''

    data = [[int(numbers) for numbers in row.split()] for row in data.splitlines()]
    checksum = 0

    for row in data:
        for i in row:
            for j in row:
                if i%j == 0 and i!=j:
                    checksum += int(i/j)
    print("The solution 2 is:", checksum)

day_2_solve1(loader("day2.txt"))
day_2_solve2(loader("day2.txt"))
