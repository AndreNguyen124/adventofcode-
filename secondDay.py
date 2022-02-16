def openFile():
    inputFile = open('text.txt', 'r')
    depths = list(inputFile.read().splitlines())

    x = ' '.join(depths)
    newList = x.split()
    return newList

def secondSolution(list):
    forward = 0
    down = 0
    for i in range(len(list)):
        count = i + 1
        if list[i].__eq__("forward"):
            value = int(list[count])
            forward += value
        elif list[i].__eq__("down"):
            value = int(list[count])
            down += value
        elif list[i].__eq__("up"):
            value = int(list[count])
            down -= value
    return forward, down

if __name__ == '__main__':
    print(openFile())
    print(secondSolution(openFile()))
