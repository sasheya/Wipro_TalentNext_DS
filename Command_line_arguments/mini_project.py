import sys

def calculateHappiness(stringOne, stringTwo, stringThree):
    count = 0
    for num in stringThree:
        if num in stringOne:
            count += 1
        if num in stringTwo:
            count -= 1
    
    return count

if(len(sys.argv) != 3):
        print("Provide three strings.")
else:
    stringOne = sys.argv[0].split('-')
    stringTwo = sys.argv[1].split('-')
    stringThree = sys.argv[2].split('-')

happiness = calculateHappiness(stringOne, stringTwo, stringThree)
print(happiness)